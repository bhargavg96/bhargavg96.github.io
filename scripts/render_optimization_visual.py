# Generate the illustrative quadratic contour plot using only Python standard library.
from pathlib import Path
import math
parts=['''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 480" role="img" aria-labelledby="title desc"><title id="title">Gradient descent on a quadratic objective</title><desc id="desc">Contours of f(x,y)=(3x²+y²)/2. Starting at (2.7,2.4), gradient descent with step size 0.14 approaches the minimum at (0,0). Each copper dot is an actual iterate.</desc><defs><clipPath id="plot"><rect x="55" y="25" width="630" height="400"/></clipPath><marker id="arrow" markerWidth="7" markerHeight="7" refX="5" refY="3.5" orient="auto"><path d="M0 0L7 3.5L0 7" fill="#b36339"/></marker></defs><rect width="720" height="480" fill="#f5f4ed"/><g clip-path="url(#plot)">''']
cx,cy,s=350,242,65
for v in [.15,.45,1,2,3.5,5.5,8,11,15,20]:
 rx=math.sqrt(2*v/3)*s;ry=math.sqrt(2*v)*s
 parts.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx:.3f}" ry="{ry:.3f}" fill="none" stroke="#638b78" stroke-width="1.3" opacity=".65"/>')
parts.append(f'<path d="M55 {cy}H685M{cx} 25V425" stroke="#c1c9bf" stroke-dasharray="3 5"/>')
for v in [-4,-3,-2,-1,1,2,3,4]:
 px=cx+v*s
 parts.append(f'<text x="{px}" y="{cy+20}" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#697970">{v}</text>')
for v in [-2,-1,1,2,3]:
 py=cy-v*s
 parts.append(f'<text x="{cx-10}" y="{py+4}" text-anchor="end" font-family="sans-serif" font-size="11" fill="#697970">{v}</text>')
points=[];x,y=2.7,2.4
for i in range(23):
 points.append((cx+x*s,cy-y*s));x-=.14*3*x;y-=.14*y
parts.append('<polyline points="'+' '.join(f'{x:.3f},{y:.3f}' for x,y in points)+'" fill="none" stroke="#b36339" stroke-width="2.5"/>')
for i,(x,y) in enumerate(points):
 if i<11 or i in [14,18,22]:parts.append(f'<circle cx="{x:.3f}" cy="{y:.3f}" r="{4 if i<11 else 2.5}" fill="#b36339" stroke="#f5f4ed" stroke-width="1.3"/>')
a,b=points[1],points[2];parts.append(f'<path d="M{a[0]} {a[1]}L{b[0]} {b[1]}" stroke="#b36339" stroke-width="2" marker-end="url(#arrow)"/>')
parts.append('</g>')
for v in [1,3.5,8]:
 angle=math.radians(145);x=cx+math.sqrt(2*v/3)*s*math.cos(angle);y=cy-math.sqrt(2*v)*s*math.sin(angle)
 parts.append(f'<text x="{x:.2f}" y="{y:.2f}" font-family="sans-serif" font-size="12" fill="#366453" stroke="#f5f4ed" stroke-width="5" paint-order="stroke">f = {v}</text>')
parts.append(f'''<circle cx="{cx}" cy="{cy}" r="5" fill="#102c35"/><text x="375" y="280" font-family="sans-serif" font-size="13" fill="#102c35">Minimum (0, 0)</text><path d="M370 269L355 248" stroke="#102c35" fill="none"/><text x="535" y="75" font-family="sans-serif" font-size="13" fill="#904f2d">Start (2.7, 2.4)</text><text x="680" y="230" font-family="Georgia,serif" font-style="italic" font-size="18" fill="#53656b">x</text><text x="363" y="37" font-family="Georgia,serif" font-style="italic" font-size="18" fill="#53656b">y</text><text x="55" y="458" font-family="sans-serif" font-size="12" fill="#53656b">Contour lines: equal objective values</text><circle cx="430" cy="454" r="4" fill="#b36339"/><text x="443" y="458" font-family="sans-serif" font-size="12" fill="#53656b">Dots: gradient-descent steps</text></svg>''')
Path('img/research/gradient-descent.svg').write_text(''.join(parts))
