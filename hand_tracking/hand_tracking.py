#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

# <rtc-template block="description">
"""
 @file hand_tracking.py
 @brief detect hand position and send to mycobot
 @date $Date$


"""
# </rtc-template>

import sys
import time
sys.path.append(".")

# Import RTM module
import RTC
import OpenRTM_aist
import cv2
import mediapipe as mp

# Import Service implementation class
# <rtc-template block="service_impl">

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">
hand_tracking_spec = ["implementation_id", "hand_tracking", 
         "type_name",         "hand_tracking", 
         "description",       "detect hand position and send to mycobot", 
         "version",           "1.0.0", 
         "vendor",            "VenderName", 
         "category",          "Actuator", 
         "activity_type",     "COMMUTATIVE", 
         "max_instance",      "1", 
         "language",          "Python", 
         "lang_type",         "SCRIPT",
         ""]
# </rtc-template>

# <rtc-template block="component_description">
##
# @class hand_tracking
# @brief detect hand position and send to mycobot
# 
# 
# </rtc-template>

class hand_tracking(OpenRTM_aist.DataFlowComponentBase):
    count = 0
    cap = 0
    hand_x, hand_y, hand_z = 0, 0, 0
    hand_xout, hand_yout, hand_zout= 0, 0, 0
    mpHands = 0
    hands = 0
    mpDraw = 0
    h, w, c = 0, 0, 0
    cx, cy, cz = 0, 0, 0
    list1 = []
    list2 = []
    grab1, grab2 = 0, 0
    grab_judge = 0
	
    ##
    # @brief constructor
    # @param manager Maneger Object
    # 
    def __init__(self, manager):
        OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

        self._d_hand_position = OpenRTM_aist.instantiateDataType(RTC.TimedFloatSeq)
        """
        """
        self._hand_positionOut = OpenRTM_aist.OutPort("hand_position", self._d_hand_position)
        self._d_grip = OpenRTM_aist.instantiateDataType(RTC.TimedShort)
        """
        """
        self._gripOut = OpenRTM_aist.OutPort("grip", self._d_grip)

        # initialize of configuration-data.
        # <rtc-template block="init_conf_param">
		
        # </rtc-template>


		 
    ##
    #
    # The initialize action (on CREATED->ALIVE transition)
    # 
    # @return RTC::ReturnCode_t
    # 
    #
    def onInitialize(self):
        # Bind variables and configuration variable
		
        # Set InPort buffers
		
        # Set OutPort buffers
        self.addOutPort("hand_position",self._hand_positionOut)
        self.addOutPort("grip",self._gripOut)
		
        # Set service provider to Ports
		
        # Set service consumers to Ports
		
        # Set CORBA Service Ports
		
        return RTC.RTC_OK
	
    ###
    ## 
    ## The finalize action (on ALIVE->END transition)
    ## 
    ## @return RTC::ReturnCode_t
    #
    ## 
    #def onFinalize(self):
    #

    #    return RTC.RTC_OK
	
    ###
    ##
    ## The startup action when ExecutionContext startup
    ## 
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onStartup(self, ec_id):
    #
    #    return RTC.RTC_OK
	
    ###
    ##
    ## The shutdown action when ExecutionContext stop
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onShutdown(self, ec_id):
    #
    #    return RTC.RTC_OK
	
    ##
    #
    # The activated action (Active state entry action)
    #
    # @param ec_id target ExecutionContext Id
    # 
    # @return RTC::ReturnCode_t
    #
    #
    def onActivated(self, ec_id):
        self._d_hand_position.data = [-0.60, -0.140, 0.180]
        self._d_grip.data = 0
    
        return RTC.RTC_OK
	
    ##
    #
    # The deactivated action (Active state exit action)
    #
    # @param ec_id target ExecutionContext Id
    #
    # @return RTC::ReturnCode_t
    #
    #
    def onDeactivated(self, ec_id):
    
        return RTC.RTC_OK
	
    ##
    #
    # The execution action that is invoked periodically
    #
    # @param ec_id target ExecutionContext Id
    #
    # @return RTC::ReturnCode_t
    #
    #
    def onExecute(self, ec_id):
        if hand_tracking.count == 0:
            hand_tracking.cap = cv2.VideoCapture(0)
            hand_tracking.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 600)
            hand_tracking.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)
            hand_tracking.mpHands = mp.solutions.hands
            hand_tracking.hands = hand_tracking.mpHands.Hands()
            hand_tracking.mpDraw = mp.solutions.drawing_utils
            hand_tracking.count = 1

        success, image = hand_tracking.cap.read()
        imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hand_tracking.hands.process(imageRGB)

        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks: # working with each hand
                for id, lm in enumerate(handLms.landmark):
                    hand_tracking.h, hand_tracking.w, hand_tracking.c = image.shape
                    hand_tracking.cx, hand_tracking.cy, hand_tracking.cz = int(lm.x * hand_tracking.w), int(lm.y * hand_tracking.h), int(lm.z * hand_tracking.h * 6)
    
                    #手の各部座標の取得
                    if id == 5:
                        hand_tracking.list1 = [hand_tracking.cx, hand_tracking.cy, hand_tracking.cz]
                    
                    if id == 9:
                        hand_tracking.grab1 = hand_tracking.cy
                
                    elif id == 12:
                        hand_tracking.grab2 = hand_tracking.cy
                
                    elif id == 17:
                        hand_tracking.list2 = [hand_tracking.cx, hand_tracking.cy, hand_tracking.cz]
                
                #trackingに使う手の座標を計算，表示
                hand_tracking.hand_x = int((hand_tracking.list1[1] + hand_tracking.list2[1])/2)
                hand_tracking.hand_y = int((hand_tracking.list1[0] + hand_tracking.list2[0])/2)
                hand_tracking.hand_z = int(((hand_tracking.list1[2] + hand_tracking.list2[2])/2) + 260)

                #cobotの可動範囲に合わせてxy座標を変換し，cobotに送るxy座標を計算
                hand_tracking.hand_xout = int(((hand_tracking.hand_x - (hand_tracking.h/2)) * 0.25) - 175)/1000
                hand_tracking.hand_yout = int(((hand_tracking.hand_y - (hand_tracking.w/2)) * 0.60) - 20)/1000
                if hand_tracking.hand_z >= 80:
                    hand_tracking.hand_zout = int(hand_tracking.hand_z) / 1000
                else :
                    hand_tracking.hand_zout = 80 / 1000

                print("send_data")
                print("x:", hand_tracking.hand_xout * 1000, "y:", hand_tracking.hand_yout * 1000, "z:", hand_tracking.hand_zout * 1000)
                cv2.circle(image, (hand_tracking.hand_y, hand_tracking.hand_x), 15, (255, 0, 255), cv2.FILLED)
                self._d_hand_position.data = [hand_tracking.hand_xout* 1000, hand_tracking.hand_yout* 1000, hand_tracking.hand_zout* 1000]

                #掴み判定(中指の根元～先の距離で判定しているので中指を曲げれば反応してしまう)
                hand_tracking.grab_judge = hand_tracking.grab1 - hand_tracking.grab2
                #print(hand_tracking.grab_judge)

                if hand_tracking.grab_judge <= 0:
                    print("grabbed!")
                    self._d_grip.data = 1
                else:
                    self._d_grip.data = 0
                print(self._d_hand_position)
                self._hand_positionOut.write()
                print("position sent")
                self._gripOut.write()
                print("grab sent")
                hand_tracking.mpDraw.draw_landmarks(image, handLms, hand_tracking.mpHands.HAND_CONNECTIONS)

        cv2.imshow("Video",image)
        cv2.waitKey(50)
    
        return RTC.RTC_OK
	
    ###
    ##
    ## The aborting action when main logic error occurred.
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onAborting(self, ec_id):
    #
    #    return RTC.RTC_OK
	
    ###
    ##
    ## The error action in ERROR state
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onError(self, ec_id):
    #
    #    return RTC.RTC_OK
	
    ###
    ##
    ## The reset action that is invoked resetting
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onReset(self, ec_id):
    #
    #    return RTC.RTC_OK
	
    ###
    ##
    ## The state update action that is invoked after onExecute() action
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##

    ##
    #def onStateUpdate(self, ec_id):
    #
    #    return RTC.RTC_OK
	
    ###
    ##
    ## The action that is invoked when execution context's rate is changed
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onRateChanged(self, ec_id):
    #
    #    return RTC.RTC_OK
	



def hand_trackingInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=hand_tracking_spec)
    manager.registerFactory(profile,
                            hand_tracking,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    hand_trackingInit(manager)

    # create instance_name option for createComponent()
    instance_name = [i for i in sys.argv if "--instance_name=" in i]
    if instance_name:
        args = instance_name[0].replace("--", "?")
    else:
        args = ""
  
    # Create a component
    comp = manager.createComponent("hand_tracking" + args)

def main():
    # remove --instance_name= option
    argv = [i for i in sys.argv if not "--instance_name=" in i]
    # Initialize manager
    mgr = OpenRTM_aist.Manager.init(sys.argv)
    mgr.setModuleInitProc(MyModuleInit)
    mgr.activateManager()
    mgr.runManager()

if __name__ == "__main__":
    main()

