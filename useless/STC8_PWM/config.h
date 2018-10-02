#ifndef		__CONFIG_H
#define		__CONFIG_H


/*********************************************************/

#define MAIN_Fosc		22118400L	//定义主时钟
//#define MAIN_Fosc		12000000L	//定义主时钟
//#define MAIN_Fosc		11059200L	//定义主时钟
//#define MAIN_Fosc		 5529600L	//定义主时钟
//#define MAIN_Fosc		24000000L	//定义主时钟


/*********************************************************/

#include	"STC15Fxxxx.H"


sbit	P_DIR_X= P1^0;		//D5	8

sbit	P_PWM_X= P1^1;		//D2	5

sbit	P_DIR_Y= P1^2;		//D6	9

sbit	P_PWM_Y= P1^3;		//D3	6

sbit	LED = P1^4;
#endif
