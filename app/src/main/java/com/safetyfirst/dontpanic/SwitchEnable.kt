package com.safetyfirst.dontpanic

import android.R
import android.widget.TextView

public class SwitchEnable extends ActionBarActivity implements CompoundButton.OnCheckedChangeListener {
    Switch enableSwitch = null;






    EnableSwitch.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
        public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {
            // do something, the isChecked will be
            // true if the switch is in the On position
        }
    });

    fun disable(){
//    TODO: Disable
    }

    fun enable(){
//    TODO: Enable
    }


    fun disableMessage(view: View) {
        (findViewById(R.id.StatusText) as TextView).text = "App Disabled: Location sharing and notifications off"
    }

    fun enableMessage(view: View) {
        (findViewById(R.id.StatusText) as TextView).text = "App Disabled: Location sharing and notifications off"
    }
}