package com.mobiserenity.formationandroid;

import android.app.Activity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

/**
 * Created by lmaignan on 13/12/2015.
 */
public class HelloActivity extends Activity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.hello_world);

        TextView mtv = (TextView)findViewById(R.id.tv);
        //mtv.setText("Nouveau text");
        mtv.setText(getResources().getString(R.string.hello_world,"(luc)"));
        mtv.setText(getResources().getString(R.string.hello_world));

        Button bt = (Button)findViewById(R.id.button2);
        bt.setOnClickListener(btListener);
    }

    private View.OnClickListener btListener = new View.OnClickListener()
    {
        @Override
        public void onClick(View v) {
            TextView tt = (TextView)findViewById(R.id.tv);
            EditText saisie = (EditText)findViewById(R.id.editText);
            tt.setText(saisie.getText().toString());

        }
    };
}
