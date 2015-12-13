package com.mobiserenity.formationandroid;

import android.app.Activity;
import android.os.Bundle;
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
        mtv.setText("Nouveau text");
        mtv.setText(getResources().getString(R.string.hello_world));
    }
}
