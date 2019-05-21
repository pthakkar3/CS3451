def setup():
    size(600, 600)
    
def draw():
    background(255, 255, 255)
    noStroke()
    a = ((float(mouseX) / 150) - 2)
    bi = ((float(mouseY) / 150) - 2) * -1
    text(a, 10, 20, 10)
    text(bi, 10, 40, 10)
    sum_real = 0
    sum_imag = 0
    power = 0
    ellipse((0 + 3) * 100, (0 + 3) * 100, 3, 3)
    fractals(a, bi, sum_real, sum_imag, power)
    
    
def fractals(v_real_prev, v_imag_prev, sum_real, sum_imag, power):
    if (power == 10):
        return
    v_new_real, v_new_imag = getToNextPower(v_real_prev, v_imag_prev, ((float(mouseX) / 150) - 2), (((float(mouseY)/150) - 2)) )
    newSumReal, newSumImag = sum_real + v_new_real, sum_imag + v_new_imag
    if (power%2 == 0):
        fill(0, 0, 255)
    else:
        fill(255, 0, 0)
    ellipse(((float(newSumReal) + 3) * 100), (((float(newSumImag) ) + 3) * 100), 3, 3)
    fractals(v_new_real, v_new_imag, newSumReal, newSumImag, power +1)
    
    v_new_real, v_new_imag = getToNextPower(v_real_prev, v_imag_prev, ((float(mouseX) / 150) - 2), (((float(mouseY)/150) - 2)))
    newSumReal, newSumImag = sum_real - v_new_real, sum_imag - v_new_imag
    if (power%2 == 0):
        fill(0, 0, 255)
    else:
        fill(255, 0, 0)
    ellipse(((float(newSumReal) + 3) * 100), (((float(newSumImag) ) + 3) * 100), 3, 3)
    fractals(v_new_real, v_new_imag, newSumReal, newSumImag, power +1)
    
def getToNextPower(v_real_prev, v_imag_prev, v_real, v_imag):
    return v_real_prev*v_real - v_imag_prev*v_imag, v_real_prev*v_imag + v_imag_prev*v_real