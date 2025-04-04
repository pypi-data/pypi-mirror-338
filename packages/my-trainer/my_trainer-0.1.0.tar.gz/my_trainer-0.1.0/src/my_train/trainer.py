import os
class Trainer():
    def __init__(self, 
                 model, 
                 loss_fn = None, 
                 optimizer = None):
        self.model = model
        self.loss_fn = loss_fn    
        self.optimizer = optimizer
        if (self.optimizer is None):
            self.optimizer = torch.optim.Adam(model.parameters, lr=0.001)
        if (self.loss_fn is None):
            self.loss_fn = torch.nn.BCELoss()

    def train(self, train_dl, 
                    val_dl, 
                    num_epochs =10, 
                    eval_freq = 100, 
                    chk_pt_freq = 200,
                    chk_pt_filepath = None):
        if (chk_pt_filepath is None):
            chk_pt_filepath = 'model_weigths.pth'
        model = self.model
        if (os.path.exists(chk_pt_filepath)):
            try:
                model.load_state_dict(torch.load(chk_pt_filepath))
            except Exception as e:
                print(f'Error while loading model weights from chk point file {e}')
        for epoch in range(num_epochs):
            model.train()
            for i, (batch, outputs, lengths) in enumerate(train_dl):
                self.optimizer.zero_grad()
                pred = model(batch, lengths)
                loss = loss_fn(pred.squeeze(), outputs)
                loss.backward()
                self.optimizer.step()
                if (i % eval_freq == 0):
                    model.eval()
                    val_loss = 0
                    for j, (batch, outputs, lengths) in enumerate(val_dl):                        
                        with torch.no_grad():
                            out = model(batch, lengths)
                            loss = loss_fn(out.squeeze(), outputs)
                            val_loss += loss
                    val_loss /= (len(val_dl))
                    print(f'Epoch {epoch}, Batch {i}, Loss {loss}, Val_Loss : {val_loss}')
                    model.train()
                if (i != 0 and i% chk_pt_freq == 0):
                    torch.save(model.state_dict(), chk_pt_filepath)
    