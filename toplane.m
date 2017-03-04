% Input 3 unique points on plane of interest.
a=[0.0, 0.0, 0.0];
b=[-11.9817, -67.9517, 0.0];
c=[-11.9817, -67.9517, 1.0];
% Do not modify below this line.
n=cross(b-a,a-c);
n=n/norm(n);
d=n(1)*(0+a(1))+n(2)*(0+a(2))+n(3)*(0+a(3)); 
disp(strcat("MCNP Line is:\n"," SURF         p ",num2str(n(1))," ",num2str(n(2))," ",num2str(n(3))," ",num2str(d)," $ COMMENT"))
