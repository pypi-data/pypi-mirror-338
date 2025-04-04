from my_rnn import RNN
from my_utils import Tokenizer, TextDataset, load_data
#from gen_text import GenerateText
from torch.utils.data import DataLoader
import torch.nn as nn
import torch.optim as optim
import torch
import os
from torch.distributions import Categorical 
from my_train import Trainer

def main():
    tknzr = Tokenizer("gpt-4")
    pad_token_id = tknzr.get_encoder().eot_token+1
    vocab_size = tknzr.get_encoder().n_vocab+1
    embedding_size = 20
    hidden_size = 30
    batch_size = 50
    seq_length = 20
    
    data = ["hello world, from transformer", "The quick brown fox jumps over the lazy dog"]
    dataset = TextDataset(data, seq_len=4)
    
    for _ in range(len(dataset)):
        print(dataset[_])

    '''
    print('stride 2')
    dataset = TextDataset(data, seq_len=4, stride=2)

    for _ in range(len(dataset)):
        print(dataset[_])   
    
    '''
    
    data = load_data("/Users/venkatkedar/personal/work/gutenberg/data/.mirror/1/0/0/0/10000/10000-0.txt")
    dataset = TextDataset(data, tokenizer=tknzr, seq_len=seq_length, pad_token_id=pad_token_id)

    val_data = load_data("/Users/venkatkedar/personal/work/gutenberg/data/.mirror/1/0/0/0/10001/10001-0.txt")
    val_data = val_data[:1000]
    val_dataset = TextDataset(val_data, tokenizer=tknzr, seq_len=seq_length, pad_token_id=pad_token_id)
    #for _ in range(10):
    #    print(dataset[_])
    
    dataloader = DataLoader(dataset, collate_fn=collate_fn, batch_size=batch_size, shuffle=False, drop_last=True)
    val_dataloader = DataLoader(val_dataset, collate_fn=collate_fn, batch_size=batch_size, shuffle=False, drop_last=True)
    print(len(dataloader))
    
    model = RNN(vocab_size=vocab_size, embed_size=embedding_size, hidden_size=hidden_size, num_layers=1)
    
    loss_fn = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)
    '''
    num_epochs = 4
    file_name = 'word_rnn.pth'
    for epoch in range(num_epochs):
        if file_name in os.listdir():
            model.load_state_dict(torch.load(file_name))
        model.train()
        for i, batch in enumerate(dataloader):
            hidden, cell = model.init_hidden(batch_size)
            optimizer.zero_grad()
            loss = 0
            if (i >10): 
                break
            for c in range(seq_length):
                #print(f'batch shape: {batch["input_ids"][:, c].shape} , contents: {batch["input_ids"][:, c]}')
                output, hidden, cell = model(batch["input_ids"][:, c], hidden, cell)
                loss += loss_fn(output, batch["labels"][:, c])                    
            loss.backward()
            optimizer.step()
            loss = loss.item() / seq_length
            if epoch % 2 == 0:
                print(f'Epoch: {epoch}, Batch: {i}, Loss: {loss}')   
            if epoch % 100 == 0:
                #print(gen_text(model, 'The island', 50, char2int=char2int, int2char=int2char))
                torch.save(model.state_dict(), file_name)

    torch.save(model.state_dict(), file_name)
    '''
    
    trainer = Trainer(model, loss_fn, optimizer)
    trainer.train(dataloader, 
                  val_dataloader,
                  num_epochs=3,
                  eval_freq = 200,
                  chk_pt_freq = 400,
                  chk_pt_filepath = 'gen_txt_model_wts.pth')
    
    tokenizer = Tokenizer("gpt-4")
    generated_text = gen_text(model, 'The island is very beautiful because ', 30, tokenizer)
    #gentxt = GenerateText(tokenizer=tokenizer)
    #prompt = "The quick brown fox jumps over the lazy dog"
    #generated_text = gentxt.generate_text(prompt)
    print(generated_text)

def gen_text(model, start_text, length, tokenizer, scale_factor=1.0):
    encoded_text = torch.tensor(tokenizer.tokenize(start_text))
    encoded_text = torch.reshape(encoded_text, (1, -1))
    hidden, cell = model.init_hidden(1)
    generated_text = start_text
    model.eval()
    print(f'encoded text: {encoded_text}')
    print(f'start text: {start_text}')
    for c in range(len(encoded_text) - 1):
        print(f'txt contents: {encoded_text[:, c]}')
        _, hidden, cell = model(encoded_text[:, c].view(1), hidden, cell)   
    
    last_word = encoded_text[:, -1].view(1)
    print(f'last word: {last_word}')
    for c in range(length):
        output, hidden, cell = model(last_word, hidden, cell)
        print(f'output shape: {output.shape}')
        logits = torch.squeeze(output, 0)
        print(f'logits contents: {logits}')
        scaled_logits = logits * scale_factor
        scaled_softmax = nn.functional.softmax(scaled_logits, dim=-1)
        m = Categorical(logits=scaled_softmax)
        print(f'scaled softmax: {scaled_softmax}')
        next_word_id = m.sample()
        print(f'next word id: {next_word_id}')
        predicted_word = tokenizer.detokenize([next_word_id.item()])
        generated_text += predicted_word
        last_word = next_word_id.view(1)    
    return generated_text

def collate_fn(batch):
    padded_batch = torch.nn.utils.rnn.pad_sequence([torch.tensor(item["input_ids"], dtype=torch.int) for item in batch], batch_first=True)
    padded_labels = torch.nn.utils.rnn.pad_sequence([torch.tensor(item["labels"], dtype=torch.int) for item in batch], batch_first=True)
    lengths = [len(item["input_ids"]) for item in batch]
    lengths = torch.tensor(lengths)
    #lengths = torch.tensor([len(seq) for seq in batch])
    return padded_batch, padded_labels, lengths