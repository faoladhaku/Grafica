# Creacion de curvas utilizando el algoritmo de Casteljau
- Codigo
  * El Algoritmo de Casteljau es programado de la siguiente forma:
  ```
  void deCas(){
	double t;
	for(t=0;t<=1.0;t=t+0.001){
		currentX=(1-t)*((1-t)*((1-t)*x[0]+t*x[1])+t*((1-t)*x[1]+t*x[2]))+t*((1-t)*((1-t)*x[1]+t*x[2])+t*((1-t)*x[2]+t*x[3]));
		currentY=(1-t)*((1-t)*((1-t)*y[0]+t*y[1])+t*((1-t)*y[1]+t*y[2]))+t*((1-t)*((1-t)*y[1]+t*y[2])+t*((1-t)*y[2]+t*y[3]));
		drawLine(oldX,720-oldY,currentX,720-currentY);
		oldX=currentX;
		oldY=currentY;
	  }
  }
  ```
- Resultado 
![alt text](https://github.com/faoladhaku/Grafica/blob/master/Tarea%20Final/grafica.png)


:+1: El codigo ejecuta 
