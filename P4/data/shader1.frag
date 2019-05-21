#define PROCESSING_TEXTURE_SHADER

#ifdef GL_ES
precision mediump float;
precision mediump int;
#endif

uniform sampler2D texture;

varying vec4 vertColor;
varying vec4 vertTexCoord;

void main() {
  float delta = 1.0/200.0;
  vec4 diffuse_color = texture2D(texture, vertTexCoord.xy);
  vec4 up = texture2D(texture, vec2(vertTexCoord.x, vertTexCoord.y + delta));
  vec4 down = texture2D(texture, vec2(vertTexCoord.x, vertTexCoord.y - delta));
  vec4 right = texture2D(texture, vec2((vertTexCoord.x + delta), vertTexCoord.y));
  vec4 left = texture2D(texture, vec2((vertTexCoord.x - delta), vertTexCoord.y));
  float average = ((diffuse_color.r * 0.3) + (diffuse_color.g * 0.6) + (diffuse_color.b * 0.1));

  float red = up.r + down.r + right.r + left.r - (4 * average);
  float green = up.g + down.g + right.g + left.g - (4 * average);
  float blue = up.b + down.b + right.b + left.b - (4 * average);
  float lap_grey = ((red * 0.3) + (green * 0.6) + (blue * 0.1));
  gl_FragColor = vec4(4*lap_grey, 4*lap_grey, 4*lap_grey, 1.0);
}
