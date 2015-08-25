package com.mobiserenity.formationandroid;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.widget.TextView;

/**
 * Created by Luc Maignan on 25/08/2015.
 */
public class ConnectedIntentActivity extends Activity {

    private TextView login;
    private TextView password;
    private final String EXTRA_LOGIN = "login";
    private final String EXTRA_PASSWORD = "password";
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.act_intent_2);
        Intent intent = getIntent();
        String loginTxt = intent.getStringExtra(EXTRA_LOGIN);
        String passwordTxt = intent.getStringExtra(EXTRA_PASSWORD);
        login = (TextView) findViewById(R.id.userLogin);
        login.setText(loginTxt);
        password = (TextView) findViewById(R.id.userPassword);
        password.setText(passwordTxt);
    }
}
