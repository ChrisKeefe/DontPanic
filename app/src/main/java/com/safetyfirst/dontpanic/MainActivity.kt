package com.safetyfirst.dontpanic

import android.os.Bundle
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import com.google.android.gms.tasks.OnCompleteListener
import com.google.firebase.iid.FirebaseInstanceId
import android.content.Intent
import android.view.View
import android.widget.Button


class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        FirebaseInstanceId.getInstance().instanceId
            .addOnCompleteListener(OnCompleteListener { task ->
                if (!task.isSuccessful) {
                    return@OnCompleteListener
                }

                // Get new Instance ID token
                val token = task.result?.token

                // Log and toast
                val msg =  token

                //UnComment out if you need the token ID for testing
                //Toast.makeText(baseContext, msg, Toast.LENGTH_LONG).show()
            })

    }

    fun openProfileActivity(view: View){
        val intent = Intent(this, createProfile::class.java)
        startActivity(intent);
    }

    fun openAboutActivity(view: View){
        val intent = Intent(this, openAboutActivity::class.java)
        startActivity(intent);
    }

}
