import numpy as np
from PIL import Image, ImageFile
import seam_carving


def parseImage(im: str):
    p = ImageFile.Parser()
    while 1:
        s = im.read(1024)
        if not s:
            break
        p.feed(s)
    im = p.close()
    return im


def cas(im: Image):
    MAX_SIZE = 400

    im = im.convert('RGB')
    im_w, im_h = im.size
    sc = min(MAX_SIZE / im_w, MAX_SIZE / im_h)
    if sc < 1:
        im = im.resize((round(im_w * sc), round(im_h * sc)))
    src = np.array(im)
    dst = src
    src_h, src_w, _ = src.shape
    dst_h, dst_w, _ = dst.shape
    frames = []
    scale = 0.99

    for i in range(100):
        dst = seam_carving.resize(dst, (dst_w * scale, dst_h * scale))
        dst_h, dst_w, _ = dst.shape
        frames.append(Image.fromarray(dst).resize((src_w, src_h)))

    Image.fromarray(src).save('images/result.gif', save_all=True, append_images=frames, optimize=False, duration=5, loop=0)
