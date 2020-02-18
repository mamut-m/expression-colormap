# Colour Mapping for Expressions
Calculates a nice colour mapping for relative expressions which is based on a formula of the kind

<img src="https://latex.codecogs.com/svg.latex?\Large&space;y=a\frac{1}{e^{b*x}}+c" title="y = a * 1/(e^(b * x )+ c" />
where a,b,c are constants that are chosen so that value differences are visually easy to compare and x represents the actual relative expression value.

We chose a mapping of the form 
<img src="https://latex.codecogs.com/svg.latex?\Large&space;y=-0.771370403777\frac{1}{e^{0.248311904856*x}}+0.988704376608" title="x=-0.771370403777\frac{1}{e^{0.248311904856*x}}+0.988704376608" />
 
After that a standard colour map is applied.

If you use this work please cite the following work:

`Chitin and chitosan remodeling defines vegetative development and Trichoderma biocontrol. Kappel, L., Münsterkötter, M., Sipos, G., Escobar Rodriguez, C.,  and S. Gruber. PLOS Pathogens. accepted 15.01.2020, in press`


