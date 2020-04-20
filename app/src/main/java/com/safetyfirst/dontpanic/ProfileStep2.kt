package com.safetyfirst.dontpanic

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View

class ProfileStep2 : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_profile_step2)
    }

    fun goHome(view: View){
        val intent = Intent(this, MainActivity::class.java)
        startActivity(intent);
    }
}
