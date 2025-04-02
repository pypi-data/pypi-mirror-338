import torch.nn as nn
from torch_geometric.nn import HeteroConv, GATv2Conv, SAGEConv
from torch_geometric.data import HeteroData

from typing import List
from .utils import HeteroMappings

class DefaultEncoder(nn.Module):
    def __init__(self):
        super().__init__()
        self.deep = False
        super().__init__()

class GNN(nn.Module):
    def __init__(self, node_embeddings: nn.ModuleList, hetero_node_type: List[str], aggr:str="sum"):
        super().__init__()
        self.deep = True
        self.device = "cuda"
        # Define HeteroConv aggregation
        self.aggr = aggr
        self.convs = nn.ModuleList()
        # Initialize the embedding dict
        self.x_dict = {node_type: embedding.weight.to(self.device) for node_type, embedding in zip(hetero_node_type,node_embeddings)}

    def forward(self, hetero_data: HeteroData):
        x_dict = self.x_dict
        edge_index_dict = {key: edge_index.to(self.device) for key, edge_index in hetero_data.edge_index_dict.items()}  # Move edges

        for conv in self.convs:
                x_dict = conv(x_dict, edge_index_dict)

        return x_dict
    

class GATEncoder(GNN):
    def __init__(self, node_embeddings: nn.ModuleList, mappings: HeteroMappings, emb_dim: int, num_gat_layers: int=2, aggr: str="sum", device: str="cuda"):
        super().__init__(node_embeddings, mappings.hetero_node_type, aggr)
        
        for layer in range(num_gat_layers):
            # Add_self_loops doesn"t work on heterogeneous graphs as per https://github.com/pyg-team/pytorch_geometric/issues/8121#issuecomment-1751129825  
            conv = HeteroConv(
                {edge_type: GATv2Conv(in_channels=-1, out_channels=emb_dim, add_self_loops=False) for edge_type in mappings.data.edge_types},
                aggr=self.aggr
            ).to(device)
            self.convs.append(conv)
        
class GCNEncoder(GNN):
    def __init__(self, node_embeddings: nn.ModuleList, mappings: HeteroMappings, emb_dim: int, num_gcn_layers: int=2, aggr: str="sum", device: str="cuda"):
        super().__init__(node_embeddings, mappings.hetero_node_type, aggr)
        for layer in range(num_gcn_layers):
            conv = HeteroConv(
                {edge_type: SAGEConv(in_channels=-1, out_channels=emb_dim, aggr="mean") for edge_type in mappings.data.edge_types},
                aggr=self.aggr
            ).to(device)
            self.convs.append(conv)
