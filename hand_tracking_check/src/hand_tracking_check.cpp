// -*- C++ -*-
// <rtc-template block="description">
/*!
 * @file  hand_tracking_check.cpp
 * @brief ModuleDescription
 *
 */
// </rtc-template>

#include "hand_tracking_check.h"

// Module specification
// <rtc-template block="module_spec">
#if RTM_MAJOR_VERSION >= 2
static const char* const hand_tracking_check_spec[] =
#else
static const char* hand_tracking_check_spec[] =
#endif
  {
    "implementation_id", "hand_tracking_check",
    "type_name",         "hand_tracking_check",
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
hand_tracking_check::hand_tracking_check(RTC::Manager* manager)
    // <rtc-template block="initializer">
  : RTC::DataFlowComponentBase(manager),
    m_hand_positionIn("hand_position", m_hand_position),
    m_gripIn("grip", m_grip)
    // </rtc-template>
{
}

/*!
 * @brief destructor
 */
hand_tracking_check::~hand_tracking_check()
{
}



RTC::ReturnCode_t hand_tracking_check::onInitialize()
{
  // Registration: InPort/OutPort/Service
  // <rtc-template block="registration">
  // Set InPort buffers
  addInPort("hand_position", m_hand_positionIn);
  addInPort("grip", m_gripIn);
  
  // Set OutPort buffer

  
  // Set service provider to Ports
  
  // Set service consumers to Ports
  
  // Set CORBA Service Ports
  
  // </rtc-template>

  // <rtc-template block="bind_config">
  // </rtc-template>

  
  return RTC::RTC_OK;
}

/*
RTC::ReturnCode_t hand_tracking_check::onFinalize()
{
  return RTC::RTC_OK;
}
*/


//RTC::ReturnCode_t hand_tracking_check::onStartup(RTC::UniqueId /*ec_id*/)
//{
//  return RTC::RTC_OK;
//}


//RTC::ReturnCode_t hand_tracking_check::onShutdown(RTC::UniqueId /*ec_id*/)
//{
//  return RTC::RTC_OK;
//}


RTC::ReturnCode_t hand_tracking_check::onActivated(RTC::UniqueId /*ec_id*/)
{
    std::cout << "compornent activated!" << "\n";
  return RTC::RTC_OK;
}


RTC::ReturnCode_t hand_tracking_check::onDeactivated(RTC::UniqueId /*ec_id*/)
{
  return RTC::RTC_OK;
}


RTC::ReturnCode_t hand_tracking_check::onExecute(RTC::UniqueId /*ec_id*/)
{
    if (m_hand_positionIn.isNew() || m_gripIn.isNew()) {
        m_hand_positionIn.read();
        m_gripIn.read();
    

        float x = m_hand_position.data[0];
        float y = m_hand_position.data[1];
        float z = m_hand_position.data[2];

        std::cout << "input data" << "\n";
        std::cout << "x:" << x << "y:" << y << "z:" << z << "\n";

        short grip = m_grip.data;

        if (grip == 1) {
            std::cout << "grabbed!" << "\n";
        }
    }

  return RTC::RTC_OK;
}


//RTC::ReturnCode_t hand_tracking_check::onAborting(RTC::UniqueId /*ec_id*/)
//{
//  return RTC::RTC_OK;
//}


//RTC::ReturnCode_t hand_tracking_check::onError(RTC::UniqueId /*ec_id*/)
//{
//  return RTC::RTC_OK;
//}


//RTC::ReturnCode_t hand_tracking_check::onReset(RTC::UniqueId /*ec_id*/)
//{
//  return RTC::RTC_OK;
//}


//RTC::ReturnCode_t hand_tracking_check::onStateUpdate(RTC::UniqueId /*ec_id*/)
//{
//  return RTC::RTC_OK;
//}


//RTC::ReturnCode_t hand_tracking_check::onRateChanged(RTC::UniqueId /*ec_id*/)
//{
//  return RTC::RTC_OK;
//}



extern "C"
{
 
  void hand_tracking_checkInit(RTC::Manager* manager)
  {
    coil::Properties profile(hand_tracking_check_spec);
    manager->registerFactory(profile,
                             RTC::Create<hand_tracking_check>,
                             RTC::Delete<hand_tracking_check>);
  }
  
}
