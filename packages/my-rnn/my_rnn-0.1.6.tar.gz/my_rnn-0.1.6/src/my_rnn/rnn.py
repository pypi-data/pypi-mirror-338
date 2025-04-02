import torch.nn as nn
import torch

class RNN(nn.Module):
    def __init__(self, vocab_size, embed_size, hidden_size, num_layers):
        super().__init__()
        self.hidden_size = hidden_size
        self.embed = nn.Embedding(vocab_size, embed_size)
        self.lstm = nn.LSTM(embed_size, hidden_size, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_size, vocab_size)

    def forward(self, x, lengths):
        x = self.embed(x)
        x = nn.utils.rnn.pack_padded_sequence(x, lengths.numpy(), enforce_sorted = False , batch_first = True)
        out, (hidden, cell) = self.lstm(x, lengths)
        out = hidden[-1, :, :]
        out = self.fc(out).reshape(out.size(0), -1)
        return out
    
    def init_hidden(self, batch_size):
        hidden = torch.zeros(self.lstm.num_layers, batch_size, self.hidden_size)
        cell = torch.zeros(self.lstm.num_layers, batch_size, self.hidden_size)
        return hidden, cell 