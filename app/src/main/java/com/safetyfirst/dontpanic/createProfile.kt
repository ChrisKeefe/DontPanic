package com.safetyfirst.dontpanic

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import kotlinx.android.synthetic.main.activity_create_profile.*

class createProfile : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_create_profile)
    }


    fun openNextStepActivity(view: View){
        val intent = Intent(this, ProfileStep2::class.java)
        startActivity(intent);
    }

    // Get input text
    //val inputText = filledTextField.editText?.text.toString()

    // filledTextField.editText?.doOnTextChanged
    //{
    //   inputText, _, _, _ ->
    // Respond to input text change
    //}
}
