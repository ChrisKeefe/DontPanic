package com.safetyfirst.dontpanic

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View

class openAboutActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_open_about)
    }

    fun goHome(view: View){
        val intent = Intent(this, MainActivity::class.java)
        startActivity(intent);
    }
}
