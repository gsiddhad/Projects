#ifndef GOURAV_H_
#define GOURAV_H_

#include <iostream.h>
#include <stdio.h>
#include <conio.h>
#include <string.h>
#include <ctype.h>
#include <fstream.h>
#include <graphics.h>
#include <dos.h>
#include <dir.h>
#include <stdlib.h>

#define port 0x33

int button, mx, my;
union REGS mi, mo;
//union SREGS s;

initmouse()
{
	mi.x.ax = 0;
	int86(0x33, &mi, &mo);
	return (mo.x.ax);
}

showmouseptr()
{
	mi.x.ax = 1;
	int86(0x33, &mi, &mo);
	return 0;
}

hidemouseptr()
{
	mi.x.ax = 2;
	int86(0x33, &mi, &mo);
	return 0;
}

getmousepos(int *button, int *mx, int *my)
{
	mi.x.ax = 3;
	int86(0x33, &mi, &mo);
	*button = mo.x.bx;
	*mx = mo.x.cx;
	*my = mo.x.dx;
	return 0;
}

/*
 void changecursor(int *shape)
 {
 \\  mi.x.ax=9;
 mi.x.bx=0;
 mi.x.cx=0;
 mi.x.dx=(unsigned)shape;
 segread(&s);
 s.es=s.ds;
 int86x(0x33,&mi,&mo,&s);
 }
 */

void initgraphic()
{
	int gd = DETECT, gm = 0;
	initgraph(&gd, &gm, "C:\\tc\\bgi");
}

void bbutton(int x1, int y1, int x2, int y2)
{
	setlinestyle(0, 0, 3);
	bar(x1, y1, x2, y2);
	setcolor(15);
	line(x1, y1, x2, y1);
	line(x1, y1, x1, y2);
	setcolor(8);
	line(x2, y1, x2, y2);
	line(x1, y2, x2, y2);
	setlinestyle(0, 0, 1);
	setcolor(0);
}

void cbutton(int x1, int y1, int r1)
{
	setlinestyle(0, 0, 1);
	circle(x1, y1, r1);
	setcolor(8);
	arc(x1, y1, 45, 225, r1);
	setcolor(15);
	arc(x1, y1, 225, 405, r1);
	setcolor(0);
}

int cursor1[32] = {
	0x0000,
	0xf00f,
	0xe007,
	0xc003,
	0x8001,
	0x0000,
	0x0000,
	0x0000,
	0x0000,
	0x0000,
	0x0000,
	0x8001,
	0xc003,
	0xe00f,
	0xf00f,
	0x0000,
	0xffff,
	0x0ff0,
	0x1ff8,
	0x3ffc,
	0x799e,
	0xf99f,
	0xffff,
	0xffff,
	0xffff,
	0xffff,
	0xffff,
	0x7ffe,
	0x3c3c,
	0x1ff8,
	0x0ff0,
	0xffff,
};

int cursor2[32] = {
	0xe00f,
	0xf10f,
	0xf81f,
	0x8c63,
	0x0001,
	0x0001,
	0x0001,
	0x0001,
	0x8003,
	0xc007,
	0xc007,
	0x8003,
	0x8003,
	0xc7c7,
	0xffff,
	0xffff,
	0x1010,
	0x0820,
	0x0440,
	0x739c,
	0xfbbe,
	0xfffe,
	0xfffe,
	0xfffe,
	0x7ffc,
	0x3ff8,
	0x3ff8,
	0x7ffc,
	0x7d7c,
	0x3838,
	0x0000,
	0x0000,
};

int cursor3[32] = {
	0xffff,
	0xffff,
	0xffff,
	0xe03f,
	0xc01e,
	0x800c,
	0x0801,
	0x8001,
	0xc003,
	0x8003,
	0x0001,
	0x8009,
	0xc01c,
	0xe03e,
	0xffff,
	0xffff,
	0x0000,
	0x0000,
	0x0000,
	0x1fc0,
	0x3fe1,
	0x7ff3,
	0xf7fe,
	0x7ffe,
	0x3ffc,
	0x7ffc,
	0xfffe,
	0x7ff6,
	0x3fe3,
	0x1fc1,
	0x0000,
	0x0000,
};

int cursor4[32] = {
	0xc003,
	0xdffb,
	0xd00b,
	0xd00b,
	0xd00b,
	0xd00b,
	0xd00b,
	0xd00b,
	0xdffb,
	0xc003,
	0xfc3f,
	0xfc3f,
	0x0000,
	0x0000,
	0x0000,
	0x0000,
	0x3ffc,
	0x2004,
	0x2ff4,
	0x2ff4,
	0x2ff4,
	0x2ff4,
	0x2ff4,
	0x2ff4,
	0x2004,
	0x3ffc,
	0x03c0,
	0x03c0,
	0xffff,
	0xffff,
	0xffff,
	0xffff,
};

#endif
