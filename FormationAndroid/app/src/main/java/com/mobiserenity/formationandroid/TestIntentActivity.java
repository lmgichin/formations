package com.mobiserenity.formationandroid;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

/**
 * Created by Luc Maignan on 25/08/2015.
 */
public class TestIntentActivity extends Activity {

    private final String EXTRA_LOGIN = "login";
    private final String EXTRA_PASSWORD = "password";
    private final String EXTRA_USER = "User";
    private final int REQUEST_PASSWORD = 0x12;
    private EditText login;
    private EditText password;
    private Button connection;

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        setContentView(R.layout.act_intent_1);
        login = (EditText) findViewById(R.id.login);
        password = (EditText) findViewById(R.id.pass);
        connection = (Button) findViewById(R.id.connect);

        connection.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                goToNextActivity();
            }
        });
    }

    private void goToNextActivity() {
        Intent intent = new Intent(TestIntentActivity.this, ConnectedIntentActivity.class);

        //intent.putExtra(EXTRA_LOGIN, login.getText().toString());
        //intent.putExtra(EXTRA_PASSWORD, password.getText().toString());

        User user = new User(login.getText().toString(), password.getText().toString());
        intent.putExtra(EXTRA_USER, user);
        //startActivity(intent);
        startActivityForResult(intent, REQUEST_PASSWORD);
        }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {

        super.onActivityResult(requestCode, resultCode, data);

        if (requestCode == REQUEST_PASSWORD) {
            if (resultCode == RESULT_OK) {
                Log.v("ActivityResult", "Result_OK : " + data.getStringExtra("NewPassword"));
            } else {
                Log.v("ActivityResult", "Result_KO");
            }
        }
    }
}
