package com.mobiserenity.formationandroid;

import android.app.Activity;
import android.test.ActivityInstrumentationTestCase2;
import android.widget.EditText;

/**
 * Created by Luc Maignan on 25/08/2015.
 */
public class TestIntentActivityTest extends ActivityInstrumentationTestCase2 {

    private Activity myActivity;
    private EditText login;

    public TestIntentActivityTest () {
        super ( TestIntentActivity.class );
    }

    @Override
    protected void setUp() throws Exception {

        super.setUp();
        myActivity = this.getActivity();
        login = (EditText) myActivity.findViewById(R.id.login);
        login.setText(myActivity.getResources().getString(R.string.login));

    }

    public void testPreconditions() {
        assertNotNull(myActivity);
        assertNotNull(login);
    }

    public void testLogin() {

        assertEquals(login.getText(),myActivity.getResources().getString(R.string.login) );
    }
}
