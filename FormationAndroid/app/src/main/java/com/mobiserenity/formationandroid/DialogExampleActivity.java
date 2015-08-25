package com.mobiserenity.formationandroid;

/**
 * Created by Luc Maignan on 24/08/2015.
 */

import android.app.Activity;
import android.app.Dialog;
import android.os.Bundle;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;

public class DialogExampleActivity extends Activity {
    private Button bouton;
    //Variable globale, au-dessus de cette valeur c'est l'autre boîte de dialogue qui s'exprime
    private final static int ENERVEMENT = 4;
    private int compteur = 0;

    private final static int ID_NORMAL_DIALOG = 0;
    private final static int ID_ENERVEE_DIALOG = 1;

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.dlg_act_1);

        bouton = (Button) findViewById(R.id.button);
        bouton.setOnClickListener(boutonClik);
    }

    private OnClickListener boutonClik = new OnClickListener() {
        @Override
        public void onClick(View v) {
            // Tant qu'on n'a pas invoqué la première boîte de dialogue 5 fois
            if(compteur < ENERVEMENT) {
                //on appelle la boîte normale
                compteur ++;
                showDialog(ID_NORMAL_DIALOG);
            } else
                showDialog(ID_ENERVEE_DIALOG);
        }
    };

    /*
     * Appelée qu'à la première création d'une boîte de dialogue
     * Les fois suivantes, on se contente de récupérer la boîte de dialogue déjà créée…
     * Sauf si la méthode « onPrepareDialog » modifie la boîte de dialogue.
    */
    @Override
    public Dialog onCreateDialog (int id) {
        Dialog box = null;
        switch(id) {
            // Quand on appelle avec l'identifiant de la boîte normale
            case ID_NORMAL_DIALOG:
                box = new Dialog(this);
                box.setTitle("Je viens tout juste de naître.");
                break;

            // Quand on appelle avec l'identifiant de la boîte qui s'énerve
            case ID_ENERVEE_DIALOG:
                box = new Dialog(this);
                box.setTitle("ET MOI ALORS ???");
        }
        return box;
    }

    @Override
    public void onPrepareDialog (int id, Dialog box) {
        if(id == ID_NORMAL_DIALOG && compteur > 1)
            box.setTitle("On est au " + compteur + "ème lancement !");
        //On ne s'intéresse pas au cas où l'identifiant vaut 1, puisque cette boîte affiche le même texte à chaque lancement
    }
}
