package com.mobiserenity.formationandroid;

/**
 * Created by Luc Maignan on 24/08/2015.
 */

import java.util.ArrayList;
import java.util.List;

import android.app.Activity;
import android.os.Bundle;
import android.widget.ArrayAdapter;
import android.widget.ListView;

public class SimpleListViewItem1Activity extends Activity {

    ListView liste = null;

    @Override
    public void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);
        setContentView(R.layout.act_list_1);

        liste = (ListView) findViewById(R.id.lv);

        List<String> matieres = new ArrayList<String>();

        matieres.add("Mathématiques");
        matieres.add("Physique");
        matieres.add("Chimie");
        matieres.add("Philosophie");

        ArrayAdapter<String> adapter = new ArrayAdapter<String>(this,
                                                android.R.layout.simple_list_item_1,
                                                matieres);
        liste.setAdapter(adapter);

    }

}
