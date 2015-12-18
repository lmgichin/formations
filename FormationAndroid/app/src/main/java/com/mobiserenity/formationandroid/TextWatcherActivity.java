package com.mobiserenity.formationandroid;

import android.app.Activity;
import android.graphics.Color;
import android.os.Bundle;
import android.text.Editable;
import android.text.TextWatcher;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

/**
 * Created by lucio on 27/08/15.
 */

public class TextWatcherActivity extends Activity implements TextWatcher {

    private EditText msg;
    private TextView textIndicator;
    private Button send;
    private final static int NBMAXCHAR = 20;

    @Override
    public void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);
        setContentView(R.layout.act_watcher);

        msg = (EditText) findViewById(R.id.msg);
        msg.addTextChangedListener(this);
        textIndicator = (TextView) findViewById(R.id.indicator);
        send = (Button) findViewById(R.id.send);
    }

    @Override
    public void afterTextChanged(Editable s) {
        final int nbChar = msg.getText().toString().length();
        final int leftChar = NBMAXCHAR - nbChar;

        if (leftChar >= 0) {

            textIndicator.setText(Integer.toString(leftChar)
                    + " caractères restants");
            textIndicator.setTextColor(Color.GREEN);
            send.setEnabled(true);

        } else {

            textIndicator.setTextColor(Color.RED);
            textIndicator.setText
                    (Integer.toString(Math.abs(leftChar))
                            + " caractères en trop");
            send.setEnabled(false);
        }

    }

    @Override
    public void beforeTextChanged(CharSequence s, int start, int count,
                                  int after) {
    }

    @Override
    public void onTextChanged(CharSequence s, int start, int
            before, int count) {
    }
}