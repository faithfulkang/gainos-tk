/* Copyright(C) 2013, GaInOS-TK by Fan Wang. All rights reserved.
 * Generated by GaInOS-TK Studio at 2013-07-18:20-05-12.
 * Don't Modify it by hand.
 * Email: parai@foxmail.com
 * URL: https://github.com/parai/gainos-tk  && http://hi.baidu.com/parai
 */


#ifndef _OSEK_CFG_H_
#define _OSEK_CFG_H_
/* =====================  MISC  ========================== */
#define FULL_PREEMPTIVE_SCHEDULE  0
#define MIXED_PREEMPTIVE_SCHEDULE 1
#define NONE_PREEMPTIVE_SCHEDULE  2
#define cfgOS_SCHEDULE_POLICY FULL_PREEMPTIVE_SCHEDULE
#define cfgOS_CONFORMANCE_CLASS ECC2
#define cfgOSEK_FIFO_QUEUE_PER_PRIORITY STD_OFF
#define cfgOS_STATUS_LEVEL OS_STATUS_EXTENDED
#define cfgOS_TK_EXTEND STD_OFF
#define cfgOS_SYSTEM_STACK_SIZE 512
#define cfgOS_SHARE_SYSTEM_STACK STD_OFF
#define CHIP_MC9S12
#if defined(CHIP_MC9S12) //9s12
#define CPU_FREQUENCY        32000000 /* HZ */
#define OSC_FREQUENCY         8000000 /* HZ */
#elif defined(CHIP_STM32F1)//stm32
#define CPU_FREQUENCY        72000000 /* HZ */
#elif defined(CHIP_AT91SAM3S)
#define CPU_FREQUENCY        64000000 /* HZ */
#elif defined(CHIP_MPC56XX)
#define CPU_FREQUENCY  64000000   /* HZ */
#define OSC_FREQUENCY  8000000    /* Oscillator Clock 8MHZ */
#endif

/* App Mode */
/* =====================  TASK  ========================== */
#define cfgOSEK_MAX_PRIO 12
#define cfgOSEK_TASK_NUM  7
#define vTask0 0
#define vTask1 1
#define vTask2 2
#define vTask3 3
#define vTask4 4
#define vTask5 5
#define vTaskStart 6
#define vTask0Pri PRIORITY(5)
#define vTask1Pri PRIORITY(5)
#define vTask2Pri PRIORITY(5)
#define vTask3Pri PRIORITY(9)
#define vTask4Pri PRIORITY(9)
#define vTask5Pri PRIORITY(9)
#define vTaskStartPri PRIORITY(3)
#define vTask0StkSz 512
#define vTask1StkSz 512
#define vTask2StkSz 512
#define vTask3StkSz 512
#define vTask4StkSz 512
#define vTask5StkSz 512
#define vTaskStartStkSz 512
#define vTask0MaxAct 0
#define vTask1MaxAct 0
#define vTask2MaxAct 0
#define vTask3MaxAct 0
#define vTask4MaxAct 0
#define vTask5MaxAct 0
#define vTaskStartMaxAct 0
#define vTask0Mode ( OSNONEAPPMODE )
#define vTask1Mode ( OSNONEAPPMODE )
#define vTask2Mode ( OSNONEAPPMODE )
#define vTask3Mode ( OSNONEAPPMODE )
#define vTask4Mode ( OSNONEAPPMODE )
#define vTask5Mode ( OSNONEAPPMODE )
#define vTaskStartMode ( OSNONEAPPMODE | OSDEFAULTAPPMODE )
#if !defined(MACROS_ONLY)
IMPORT TASK(vTask0);
IMPORT TASK(vTask1);
IMPORT TASK(vTask2);
IMPORT TASK(vTask3);
IMPORT TASK(vTask4);
IMPORT TASK(vTask5);
IMPORT TASK(vTaskStart);
#endif
/* =====================  EVENT ========================== */
#define ID_vTask0Event 0
#define vTask0Event0 0x1
#define vTask0Event1 0x2
#define ID_vTask1Event 1
#define vTask1Event0 0x1
#define ID_vTask2Event 2
#define vTask2Event0 0x1
#define ID_vTask3Event 3
#define vTask3Event0 0x1
#define ID_vTask4Event 4
#define vTask4Event0 0x1
#define ID_vTask5Event 5
#define vTask5Event0 0x1
#define cfgOSEK_EVENTFLAG_NUM 6

/* =====================  ALARM ========================== */
#define cfgOSEK_COUNTER_NUM 1
#define SystemTimer 0
#define cfgOSEK_ALARM_NUM 0
#if !defined(MACROS_ONLY)
#endif
/*  ====================  RESOURCE ======================= */
#define cfgOSEK_RESOURCE_NUM 1
#define RES_SCHEDULER 0
#define RES_SCHEDULERPri PRIORITY(cfgOSEK_MAX_PRIO)
	//it had been assigned to [ ]

/*  ================   INTERNAL RESOURCE ================= */
#define cfgOSEK_INTERNAL_RESOURCE_NUM 0

/*  ====================  HOOKs    ======================= */
#define cfgOS_STACK_USAGE_CHECK STD_OFF
#define cfgOS_SHUT_DOWN_HOOK STD_OFF
#define cfgOS_START_UP_HOOK STD_OFF
#define cfgOS_ERROR_HOOK STD_ON
#define cfgOS_PRE_TASK_HOOK STD_OFF
#define cfgOS_POST_TASK_HOOK STD_OFF
#endif /* _OSEK_CFG_H_ */

