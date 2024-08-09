# 必要なモジュールをインポートします
import torch  # PyTorchライブラリをインポート。深層学習モデルの構築と訓練に使用します。
from torchvision import transforms  # torchvisionから画像変換用のモジュールをインポート
from PIL import Image  # Python Imaging Library (PIL) から Image モジュールをインポート。画像の読み込みと操作に使用します。
from .swin_transformer import SwinTransformerForMNIST  # 同じディレクトリにある swin_transformer.py から SwinTransformerForMNIST クラスをインポート

# 画像パスを受け取り、予測された数字を返す関数を定義します
def predict_digit(image_path):
    # SwinTransformerForMNIST モデルのインスタンスを作成します
    model = SwinTransformerForMNIST()
    # 事前に学習済みの重みをファイルから読み込みます。CPUデバイスを指定しています。
    model.load_state_dict(torch.load('ml_model/swin_transformer_mnist.pth', map_location=torch.device('cpu')))
    # モデルを評価モードに設定します。これにより、訓練時固有の動作（例：ドロップアウト）が無効化されます。
    model.eval()

    # 画像の前処理パイプラインを定義します
    transform = transforms.Compose([
        transforms.Resize((32, 32)),  # 画像を32x32ピクセルにリサイズ
        transforms.ToTensor(),  # PIL Image をテンソルに変換
        transforms.Normalize((0.1307,), (0.3081,))  # MNISTデータセットの平均と標準偏差で正規化
    ])

    # 指定されたパスから画像を開き、グレースケールに変換します
    image = Image.open(image_path).convert('L')
    # 画像に前処理を適用し、バッチ次元を追加します（モデル入力用）
    image = transform(image).unsqueeze(0)

    # 勾配計算を無効化してメモリ使用量を削減し、推論速度を向上させます
    with torch.no_grad():
        # モデルに画像を入力し、出力を取得します
        output = model(image)
        # 出力テンソルから最大値とそのインデックス（予測されたクラス）を取得します
        _, predicted = torch.max(output, 1)

    # 予測されたクラス（数字）を整数として返します
    return predicted.item()