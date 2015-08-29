package com.mobiserenity.formationandroid;

import android.app.Activity;
import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.telephony.SmsManager;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

/**
 * Created by lucio on 29/08/15.
 */
public class SMSActivity extends Activity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.act_sms);

        Button sendSms = (Button) findViewById(R.id.sendSMS);

        sendSms.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                EditText msg = (EditText) findViewById(R.id.msg);
                EditText no = (EditText) findViewById(R.id.notel);

                /* Version appli par défaut

                Intent sendSms = new Intent(Intent.ACTION_SENDTO,
                        Uri.parse("sms:" +  no.getText().toString()));
                sendSms.putExtra("sms_body", msg.getText().toString() );

                startActivity(sendSms); ***/

                SmsManager smsManager = SmsManager.getDefault();

                smsManager.sendTextMessage(no.getText().toString(), null, msg.getText().toString(), null, null);
                finish();
            }
        });
    }
}
