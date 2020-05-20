from colorsys import rgb_to_hsv, hsv_to_rgb

"""
Create a linear color ramp through HSV space.

startColor and endColor are the two ends of the color ramp in RGB space and set as a tuple of (r,g,b) where each chroma can be from 0-255.

startVal and endVal are the values that the start and end colors represent. (and should be min/max values submitted to the ramp, everything above and below will be clipped)

Once initialized, submit values to getColor() and get an RGB tuple that represents that value.

"""


class ColorRamp:
    def __init__(self, startColor, startVal, endColor, endVal, clockwise=True):
        if endVal < startVal:
            startColor, endColor = endColor, startColor
            startVal, endVal = endVal, startVal
            clockwise = not clockwise
            
        self.minVal = startVal
        self.maxVal = endVal
        self.dv = self.maxVal - self.minVal
        self.baseHsv = rgb_to_hsv(*[float(c)/255. for c in startColor])
        endHsv = rgb_to_hsv(*[float(c)/255. for c in endColor])
        if clockwise:
            if self.baseHsv[0] > endHsv[0]:
                endHsv = (endHsv[0]+1.0, endHsv[1], endHsv[2])
        else:
            if self.baseHsv[0] < endHsv[0]:
                self.baseHsv = (self.baseHsv[0]+1.0, self.baseHsv[1], self.baseHsv[2])
        self.dHsv = [e-b for b,e in zip(self.baseHsv, endHsv)]

    def getColor(self, val):
        val = (val - self.minVal) / self.dv
        if val < 0.:
            val = 0.
        if val > 1.:
            val = 1.

        rgb = hsv_to_rgb(*[val * d + b for b,d in zip(self.baseHsv, self.dHsv)])
        return [int(c * 255.5) for c in rgb]

