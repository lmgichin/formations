package com.mobiserenity.formationandroid;

/**
 * Created by Luc Maignan on 24/08/2015.
 */

import java.util.ArrayList;
import java.util.List;

import android.app.Activity;
import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.widget.Toast;

public class SimpleListViewItem1Activity extends Activity implements AdapterView.OnItemClickListener, AdapterView.OnItemLongClickListener{

    ListView liste = null;
    List<String> matieres = null;

    @Override
    public void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);
        setContentView(R.layout.act_list_1);

        liste = (ListView) findViewById(R.id.lv);

        matieres = new ArrayList<String>();

        matieres.add("Mathématiques 1");
        matieres.add("Physique 1");
        matieres.add("Chimie 1");
        matieres.add("Philosophie 1");
        matieres.add("Mathématiques 2");
        matieres.add("Physique 2");
        matieres.add("Chimie 2");
        matieres.add("Philosophie 2");
        matieres.add("Mathématiques 3");
        matieres.add("Physique 3");
        matieres.add("Chimie 3");
        matieres.add("Philosophie 3");
        matieres.add("Mathématiques 4");
        matieres.add("Physique 4");
        matieres.add("Chimie 4");
        matieres.add("Philosophie 4");

        ArrayAdapter<String> adapter = new ArrayAdapter<String>(this,
                android.R.layout.simple_list_item_1,
                matieres);

        liste.setAdapter(adapter);
        liste.setOnItemClickListener(this);
        liste.setOnItemLongClickListener(this);

    }


    @Override
    public void onItemClick(AdapterView<?> parent, View view, int position, long id) {

        Toast.makeText(this, matieres.get(position),
                Toast.LENGTH_SHORT).show();
    }

    @Override
    public boolean onItemLongClick(AdapterView<?> parent, View view, int position, long id) {
        Toast.makeText(this, "LONG : " + matieres.get(position), Toast.LENGTH_SHORT).show();
        return true;
    }
}
