// -*- C++ -*-
// <rtc-template block="description">
/*!
 * @file  hand_tracking_checkTest.cpp
 * @brief ModuleDescription (test code)
 *
 */
// </rtc-template>

#include "hand_tracking_checkTest.h"

// Module specification
// <rtc-template block="module_spec">
#if RTM_MAJOR_VERSION >= 2
static const char* const hand_tracking_check_spec[] =
#else
static const char* hand_tracking_check_spec[] =
#endif
  {
    "implementation_id", "hand_tracking_checkTest",
    "type_name",         "hand_tracking_checkTest",
    "description",       "ModuleDescription",
    "version",           "1.0.0",
    "vendor",            "VenderName",
    "category",          "Category",
    "activity_type",     "PERIODIC",
    "kind",              "DataFlowComponent",
    "max_instance",      "1",
    "language",          "C++",
    "lang_type",         "compile",
    ""
  };
// </rtc-template>

/*!
 * @brief constructor
 * @param manager Maneger Object
 */
hand_tracking_checkTest::hand_tracking_checkTest(RTC::Manager* manager)
    // <rtc-template block="initializer">
  : RTC::DataFlowComponentBase(manager),
    m_hand_positionOut("hand_position", m_hand_position),
    m_gripOut("grip", m_grip)

    // </rtc-template>
{
}

/*!
 * @brief destructor
 */
hand_tracking_checkTest::~hand_tracking_checkTest()
{
}



RTC::ReturnCode_t hand_tracking_checkTest::onInitialize()
{
  // Registration: InPort/OutPort/Service
  // <rtc-template block="registration">
  // Set InPort buffers
  
  // Set OutPort buffer
  addOutPort("hand_position", m_hand_positionOut);
  addOutPort("grip", m_gripOut);
  
  // Set service provider to Ports
  
  // Set service consumers to Ports
  
  // Set CORBA Service Ports
  
  // </rtc-template>

  // <rtc-template block="bind_config">
  // </rtc-template>
  
  return RTC::RTC_OK;
}

/*
RTC::ReturnCode_t hand_tracking_checkTest::onFinalize()
{
  return RTC::RTC_OK;
}
*/


//RTC::ReturnCode_t hand_tracking_checkTest::onStartup(RTC::UniqueId /*ec_id*/)
//{
//  return RTC::RTC_OK;
//}


//RTC::ReturnCode_t hand_tracking_checkTest::onShutdown(RTC::UniqueId /*ec_id*/)
//{
//  return RTC::RTC_OK;
//}


RTC::ReturnCode_t hand_tracking_checkTest::onActivated(RTC::UniqueId /*ec_id*/)
{
  return RTC::RTC_OK;
}


RTC::ReturnCode_t hand_tracking_checkTest::onDeactivated(RTC::UniqueId /*ec_id*/)
{
  return RTC::RTC_OK;
}


RTC::ReturnCode_t hand_tracking_checkTest::onExecute(RTC::UniqueId /*ec_id*/)
{
  return RTC::RTC_OK;
}


//RTC::ReturnCode_t hand_tracking_checkTest::onAborting(RTC::UniqueId /*ec_id*/)
//{
//  return RTC::RTC_OK;
//}


//RTC::ReturnCode_t hand_tracking_checkTest::onError(RTC::UniqueId /*ec_id*/)
//{
//  return RTC::RTC_OK;
//}


//RTC::ReturnCode_t hand_tracking_checkTest::onReset(RTC::UniqueId /*ec_id*/)
//{
//  return RTC::RTC_OK;
//}


//RTC::ReturnCode_t hand_tracking_checkTest::onStateUpdate(RTC::UniqueId /*ec_id*/)
//{
//  return RTC::RTC_OK;
//}


//RTC::ReturnCode_t hand_tracking_checkTest::onRateChanged(RTC::UniqueId /*ec_id*/)
//{
//  return RTC::RTC_OK;
//}


bool hand_tracking_checkTest::runTest()
{
    return true;
}


extern "C"
{
 
  void hand_tracking_checkTestInit(RTC::Manager* manager)
  {
    coil::Properties profile(hand_tracking_check_spec);
    manager->registerFactory(profile,
                             RTC::Create<hand_tracking_checkTest>,
                             RTC::Delete<hand_tracking_checkTest>);
  }
  
}
