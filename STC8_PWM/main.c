#include	"config.h"
#include	"USART1.h"
#include	"delay.h"
#include	"timer.h"

/*************	功能说明	**************

双串口全双工中断方式收发通讯程序。

通过PC向MCU发送数据, MCU收到后通过串口把收到的数据原样返回.

******************************************/

/*************	本地常量声明	**************/
#define		PWM_DUTY		6000			//定义PWM的周期，数值为时钟周期数，假如使用24.576MHZ的主频，则PWM频率为6000HZ。

#define		PWM_HIGH_MIN	32				//限制PWM输出的最小占空比。用户请勿修改。
#define		PWM_HIGH_MAX	(PWM_DUTY-PWM_HIGH_MIN)	//限制PWM输出的最大占空比。用户请勿修改。

/*************	本地变量声明	**************/

double omega_x,omega_y;

/*************	本地函数声明	**************/



/************************ 定时器配置 ****************************/
void	Timer_config(void) //初始化Timer0	  Timer0,Timer1,Timer2
{
	
	
	TIM_InitTypeDef		TIM_InitStructure;					//结构定义
	
	
	
	TIM_InitStructure.TIM_Mode      = TIM_16BitAutoReload;	//指定工作模式,   TIM_16BitAutoReload,TIM_16Bit,TIM_8BitAutoReload,TIM_16BitAutoReloadNoMask
	TIM_InitStructure.TIM_Polity    = PolityHigh;			//指定中断优先级, PolityHigh,PolityLow
	TIM_InitStructure.TIM_Interrupt = ENABLE;				//中断是否允许,   ENABLE或DISABLE
	TIM_InitStructure.TIM_ClkSource = TIM_CLOCK_1T;			//指定时钟源,     TIM_CLOCK_1T,TIM_CLOCK_12T,TIM_CLOCK_Ext
	TIM_InitStructure.TIM_ClkOut    = ENABLE;				//是否输出高速脉冲, ENABLE或DISABLE
	TIM_InitStructure.TIM_Value     = 65536UL - PWM_HIGH_MIN;	//初值,
	TIM_InitStructure.TIM_Run       = ENABLE;				//是否初始化后启动定时器, ENABLE或DISABLE
	Timer_Inilize(Timer0,&TIM_InitStructure);				//初始化Timer0	  Timer0,Timer1,Timer2

					//结构定义
	TIM_InitStructure.TIM_Mode      = TIM_16BitAutoReload;	//指定工作模式,   TIM_16BitAutoReload,TIM_16Bit,TIM_8BitAutoReload,TIM_16BitAutoReloadNoMask
	TIM_InitStructure.TIM_Polity    = PolityHigh;			//指定中断优先级, PolityHigh,PolityLow
	TIM_InitStructure.TIM_Interrupt = ENABLE;				//中断是否允许,   ENABLE或DISABLE
	TIM_InitStructure.TIM_ClkSource = TIM_CLOCK_1T;			//指定时钟源,     TIM_CLOCK_1T,TIM_CLOCK_12T,TIM_CLOCK_Ext
	TIM_InitStructure.TIM_ClkOut    = ENABLE;				//是否输出高速脉冲, ENABLE或DISABLE
	TIM_InitStructure.TIM_Value     = 65536UL - PWM_HIGH_MIN;	//初值,
	TIM_InitStructure.TIM_Run       = ENABLE;				//是否初始化后启动定时器, ENABLE或DISABLE
	Timer_Inilize(Timer1,&TIM_InitStructure);
}





/*************  外部函数和变量声明 *****************/


/*************  串口1初始化函数 *****************/
void	UART_config(void)
{
	COMx_InitDefine		COMx_InitStructure;					//结构定义
	COMx_InitStructure.UART_Mode      = UART_8bit_BRTx;		//模式,       UART_ShiftRight,UART_8bit_BRTx,UART_9bit,UART_9bit_BRTx
	COMx_InitStructure.UART_BRT_Use   = BRT_Timer2;			//使用波特率,   BRT_Timer1, BRT_Timer2 (注意: 串口2固定使用BRT_Timer2)
	COMx_InitStructure.UART_BaudRate  = 115200ul;			//波特率, 一般 110 ~ 115200
	COMx_InitStructure.UART_RxEnable  = ENABLE;				//接收允许,   ENABLE或DISABLE
	COMx_InitStructure.BaudRateDouble = DISABLE;			//波特率加倍, ENABLE或DISABLE
	COMx_InitStructure.UART_Interrupt = ENABLE;				//中断允许,   ENABLE或DISABLE
	COMx_InitStructure.UART_Polity    = PolityLow;			//中断优先级, PolityLow,PolityHigh
	COMx_InitStructure.UART_P_SW      = UART1_SW_P30_P31;	//切换端口,   UART1_SW_P30_P31,UART1_SW_P36_P37,UART1_SW_P16_P17(必须使用内部时钟)
	COMx_InitStructure.UART_RXD_TXD_Short = DISABLE;		//内部短路RXD与TXD, 做中继, ENABLE,DISABLE
	USART_Configuration(USART1, &COMx_InitStructure);		//初始化串口1 USART1,USART2

	PrintString1("STC15F2K60S2 UART1 Test Prgramme!\r\n");	//SUART1发送一个字符串
}


/**************** 计算PWM重装值函数 *******************/
void	LoadPWM(double omega_x,double omega_y)
{
	double f_x,f_y;
	double t_x,t_y;
	double derect;
	
	derect = 800;
//omega*derect>=MAIN_Fosc/65536=22118400 / 65536 = 303
	//omega>=30/80
	
	if(omega_x<0.4) 
		stop_x = 1 ;
	else
	{
		f_x = omega_x*derect/1.8;
		t_x = 1000/2/f_x;
		t_x = t_x/1000;
		PWM_x = (int)(65536-t_x*MAIN_Fosc);
	}
	
	
	if(omega_y<0.4) stop_y = 1 ;
	else
	{
		f_y = omega_y*derect/1.8;
		t_y = 1000/2/f_y;
		t_y = t_y/1000;
		PWM_y = (int)(65536-t_y*MAIN_Fosc);
	}
	
	
	
}
/**********************************************/
void main(void)
{
	u8	i;


	omega_x = 1 ;
	omega_y = 1 ;
	stop_x  = 1 ;
	stop_x  = 1 ;
	
	P_PWM_X = 0;  //Timer0
	P_PWM_Y = 0;  //Timer1
	P1M1 &= ~(1 << 4);	//P1.4 设置为推挽输出	STC15W204S
	P1M0 |=  (1 << 4);			

	Timer_config();	  
	UART_config();
	
	TR1 = 1;
	
	EA = 1;

	while (1)
	{

	delay_ms(100);

	//PrintString1("Fuck1!\r\n");

						if(COM1.RX_TimeOut > 0)		//超时计数
						{
							if(--COM1.RX_TimeOut == 0)
							{
								if(COM1.RX_Cnt > 0)
								{
									//TX1_write2buff(RX1_Buffer[0];
									//TX1_write2buff(RX1_Buffer[1];
									for(i=0; i<COM1.RX_Cnt; i++)	TX1_write2buff(RX1_Buffer[i]);//收到的数据原样返回	
									omega_x = ((RX1_Buffer[1]-48)*10+(RX1_Buffer[2]-48))/10;
									omega_y = ((RX1_Buffer[3]-48)*10+(RX1_Buffer[4]-48))/10;
									stop_x  = 0 ;
									stop_y  = 0 ;
								}
								COM1.RX_Cnt = 0;
							}
						} 	
						
		//$aabb



						
		LoadPWM(omega_x,omega_y);

		delay_ms(100);

	}
}



