#define PROCESSING_COLOR_SHADER

#ifdef GL_ES
precision mediump float;
precision mediump int;
#endif

varying vec4 vertColor;
varying vec4 vertTexCoord;

void main() {
  float cx = (vertTexCoord.x * 3.0) - 2.1;
  float cy = (vertTexCoord.y * 3.0) - 1.5;
  float a = 0.0;
  float b = 0.0;
  for(int i = 0; i < 20; i++) {
      float newa = (a * a) - (b * b) + cx;
      float newb = (2.0 * a * b) + cy;
      a = newa;
      b = newb;
  }

  if (((a*a) + (b*b)) <= 2) {
    gl_FragColor = vec4(1.0, 1.0, 1.0, 1.0);
  } else {
    gl_FragColor = vec4(1.0, 0.0, 0.0, 1.0);
  }
  
}
