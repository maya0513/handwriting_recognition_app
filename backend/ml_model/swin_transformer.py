import torch.nn as nn
from timm.models.swin_transformer import SwinTransformer

class SwinTransformerForMNIST(nn.Module):
    def __init__(self):
        super(SwinTransformerForMNIST, self).__init__()
        self.swin = SwinTransformer(
            img_size=32,
            patch_size=2,
            in_chans=1,
            num_classes=10,
            embed_dim=32,
            depths=[2, 2, 2],
            num_heads=[2, 4, 8],
            window_size=4,
            mlp_ratio=2.0,
            qkv_bias=True,
            drop_rate=0.1,
            attn_drop_rate=0.1,
            drop_path_rate=0.1,
        )

    def forward(self, x):
        return self.swin(x)