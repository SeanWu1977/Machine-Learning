### 接著face_reocognition 安裝
```
pip3 install torch==1.2.0+cpu torchvision==0.4.0+cpu -f https://download.pytorch.org/whl/torch_stable.html
pip3 install git+https://github.com/tkat0/PyTorch_BlazeFace

#測試是否安裝成功

cmd下：
python3


>> import torch
>> from blazeface import BlazeFace
>> x = torch.randn(1, 3, 128, 128)
>> model = BlazeFace()
>> h = model(x)
>> h

tensor([[[[6.3361e+00, 2.9726e+00, 5.1237e+00,  ..., 5.6183e+00,
           5.9961e+00, 4.5983e+00],
          [3.0893e+00, 8.8182e+00, 7.2421e+00,  ..., 6.5477e+00,
           6.9388e+00, 7.5560e+00],
          [1.8872e+00, 4.5485e+00, 3.5757e+00,  ..., 4.3431e+00,
           5.0710e+00, 4.1762e+00],
          ...,
          [5.2779e+00, 7.3559e+00, 4.7028e+00,  ..., 7.9480e+00,
           1.1822e+01, 6.8175e+00],
          [3.9745e+00, 9.7064e+00, 4.7488e+00,  ..., 1.0799e+01,
           1.1051e+01, 7.6042e+00],
          [7.9075e+00, 5.9418e+00, 8.4335e+00,  ..., 1.0781e+01,
           5.8763e+00, 1.0059e+01]],

         [[8.7968e+00, 8.3394e+00, 7.3307e+00,  ..., 5.6626e+00,
           7.2955e+00, 5.1054e+00],
          [6.1625e+00, 7.6080e+00, 9.4624e+00,  ..., 4.9363e+00,
           3.6947e+00, 4.5362e+00],
          [2.0220e+00, 4.0261e+00, 8.7629e+00,  ..., 6.0215e+00,
           1.4991e+00, 5.8214e+00],
          ...,
          [4.4036e+00, 9.8168e+00, 2.8466e+00,  ..., 1.1178e+01,

```
