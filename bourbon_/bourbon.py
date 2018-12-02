import math

from optimeyes import haarFaceCascade, haarEyeCascade, detect, getOffset, getLeftAndRightEyes, containsPoint


def get_err(x, y, x_f, y_f, t):
    return abs(x_f(t) - x) + abs(y_f(t) - y)


def rate_drunkenness(vid, x_f, y_f, fps):
    err = 0
    offsets = vid_to_offsets(vid)
    for i, offset in enumerate(offsets):
        if offset:
            t = (1/fps)*i
            x, y = offset[0], offset[1]
            err += get_err(x, y, x_f, y_f, t)
    return err


def sinusoid(t, max_t, step):
    return max_t + math.sin(t*step - math.pi)


def get_parametric_functions(min_offset, max_offset, step):
    min_x, min_y = min_offset[0], min_offset[1]
    max_x, max_y = max_offset[0], max_offset[1]
    vec_x, vec_y = (max_x - min_x), (max_y - min_y)

    def x_f(x): return min_x + (vec_x*sinusoid(x, max_x, step))

    def y_f(y): return min_y + (vec_y*sinusoid(y, max_y, step))
    return x_f, y_f


def vid_to_offsets(vid):
    offsets = []
    ok, frame = vid.read()
    while ok:
        offset = getOffset(frame, haarFaceCascade, haarEyeCascade)
        if offset:
            offsets.append((offset[0], offset[1]))
        else:
            offsets.append(None)
        ok, frame = vid.read()
    return offsets


def calibrate(min, max, step):
    min_offset = getOffset(min, haarFaceCascade, haarEyeCascade)
    max_offset = getOffset(max, haarFaceCascade, haarEyeCascade)
    if not min_offset or not max_offset:
        return None
    return get_parametric_functions(min_offset, max_offset, step)
