#include	"config.h"
#include	"USART1.h"
#include	"delay.h"
#include	"timer.h"

/*************	����˵��	**************

˫����ȫ˫���жϷ�ʽ�շ�ͨѶ����

ͨ��PC��MCU��������, MCU�յ���ͨ�����ڰ��յ�������ԭ������.

******************************************/

/*************	���س�������	**************/
#define		PWM_DUTY		6000			//����PWM�����ڣ���ֵΪʱ��������������ʹ��24.576MHZ����Ƶ����PWMƵ��Ϊ6000HZ��

#define		PWM_HIGH_MIN	32				//����PWM�������Сռ�ձȡ��û������޸ġ�
#define		PWM_HIGH_MAX	(PWM_DUTY-PWM_HIGH_MIN)	//����PWM��������ռ�ձȡ��û������޸ġ�

/*************	���ر�������	**************/

double omega_x,omega_y;

/*************	���غ�������	**************/



/************************ ��ʱ������ ****************************/
void	Timer_config(void) //��ʼ��Timer0	  Timer0,Timer1,Timer2
{
	
	
	TIM_InitTypeDef		TIM_InitStructure;					//�ṹ����
	
	
	
	TIM_InitStructure.TIM_Mode      = TIM_16BitAutoReload;	//ָ������ģʽ,   TIM_16BitAutoReload,TIM_16Bit,TIM_8BitAutoReload,TIM_16BitAutoReloadNoMask
	TIM_InitStructure.TIM_Polity    = PolityHigh;			//ָ���ж����ȼ�, PolityHigh,PolityLow
	TIM_InitStructure.TIM_Interrupt = ENABLE;				//�ж��Ƿ�����,   ENABLE��DISABLE
	TIM_InitStructure.TIM_ClkSource = TIM_CLOCK_1T;			//ָ��ʱ��Դ,     TIM_CLOCK_1T,TIM_CLOCK_12T,TIM_CLOCK_Ext
	TIM_InitStructure.TIM_ClkOut    = ENABLE;				//�Ƿ������������, ENABLE��DISABLE
	TIM_InitStructure.TIM_Value     = 65536UL - PWM_HIGH_MIN;	//��ֵ,
	TIM_InitStructure.TIM_Run       = ENABLE;				//�Ƿ��ʼ����������ʱ��, ENABLE��DISABLE
	Timer_Inilize(Timer0,&TIM_InitStructure);				//��ʼ��Timer0	  Timer0,Timer1,Timer2

					//�ṹ����
	TIM_InitStructure.TIM_Mode      = TIM_16BitAutoReload;	//ָ������ģʽ,   TIM_16BitAutoReload,TIM_16Bit,TIM_8BitAutoReload,TIM_16BitAutoReloadNoMask
	TIM_InitStructure.TIM_Polity    = PolityHigh;			//ָ���ж����ȼ�, PolityHigh,PolityLow
	TIM_InitStructure.TIM_Interrupt = ENABLE;				//�ж��Ƿ�����,   ENABLE��DISABLE
	TIM_InitStructure.TIM_ClkSource = TIM_CLOCK_1T;			//ָ��ʱ��Դ,     TIM_CLOCK_1T,TIM_CLOCK_12T,TIM_CLOCK_Ext
	TIM_InitStructure.TIM_ClkOut    = ENABLE;				//�Ƿ������������, ENABLE��DISABLE
	TIM_InitStructure.TIM_Value     = 65536UL - PWM_HIGH_MIN;	//��ֵ,
	TIM_InitStructure.TIM_Run       = ENABLE;				//�Ƿ��ʼ����������ʱ��, ENABLE��DISABLE
	Timer_Inilize(Timer1,&TIM_InitStructure);
}





/*************  �ⲿ�����ͱ������� *****************/


/*************  ����1��ʼ������ *****************/
void	UART_config(void)
{
	COMx_InitDefine		COMx_InitStructure;					//�ṹ����
	COMx_InitStructure.UART_Mode      = UART_8bit_BRTx;		//ģʽ,       UART_ShiftRight,UART_8bit_BRTx,UART_9bit,UART_9bit_BRTx
	COMx_InitStructure.UART_BRT_Use   = BRT_Timer2;			//ʹ�ò�����,   BRT_Timer1, BRT_Timer2 (ע��: ����2�̶�ʹ��BRT_Timer2)
	COMx_InitStructure.UART_BaudRate  = 115200ul;			//������, һ�� 110 ~ 115200
	COMx_InitStructure.UART_RxEnable  = ENABLE;				//��������,   ENABLE��DISABLE
	COMx_InitStructure.BaudRateDouble = DISABLE;			//�����ʼӱ�, ENABLE��DISABLE
	COMx_InitStructure.UART_Interrupt = ENABLE;				//�ж�����,   ENABLE��DISABLE
	COMx_InitStructure.UART_Polity    = PolityLow;			//�ж����ȼ�, PolityLow,PolityHigh
	COMx_InitStructure.UART_P_SW      = UART1_SW_P30_P31;	//�л��˿�,   UART1_SW_P30_P31,UART1_SW_P36_P37,UART1_SW_P16_P17(����ʹ���ڲ�ʱ��)
	COMx_InitStructure.UART_RXD_TXD_Short = DISABLE;		//�ڲ���·RXD��TXD, ���м�, ENABLE,DISABLE
	USART_Configuration(USART1, &COMx_InitStructure);		//��ʼ������1 USART1,USART2

	PrintString1("STC15F2K60S2 UART1 Test Prgramme!\r\n");	//SUART1����һ���ַ���
}


/**************** ����PWM��װֵ���� *******************/
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
	P1M1 &= ~(1 << 4);	//P1.4 ����Ϊ�������	STC15W204S
	P1M0 |=  (1 << 4);			

	Timer_config();	  
	UART_config();
	
	TR1 = 1;
	
	EA = 1;

	while (1)
	{

	delay_ms(100);

	//PrintString1("Fuck1!\r\n");

						if(COM1.RX_TimeOut > 0)		//��ʱ����
						{
							if(--COM1.RX_TimeOut == 0)
							{
								if(COM1.RX_Cnt > 0)
								{
									//TX1_write2buff(RX1_Buffer[0];
									//TX1_write2buff(RX1_Buffer[1];
									for(i=0; i<COM1.RX_Cnt; i++)	TX1_write2buff(RX1_Buffer[i]);//�յ�������ԭ������	
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



