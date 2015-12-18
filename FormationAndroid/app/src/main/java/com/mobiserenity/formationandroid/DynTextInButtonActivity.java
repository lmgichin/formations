package com.mobiserenity.formationandroid;

import android.app.Activity;
import android.os.Bundle;
import android.view.MotionEvent;
import android.view.View;
import android.widget.Button;

/**
 * Created by Luc Maignan on 24/08/2015.
 */

// On fait implémenter OnTouchListener par notre activité
public class DynTextInButtonActivity extends Activity implements View.OnTouchListener {

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        setContentView(R.layout.activity_linear_1);

        // On récupère le bouton par son identifiant
        Button b = (Button) findViewById(R.id.bouton);
        // Puis on lui indique que cette classe sera son listener pour l'évènement Touch
        b.setOnTouchListener(this);
    }

    // Fonction qui sera lancée à chaque fois qu'un toucher est détecté sur le bouton rattaché
    @Override
    public boolean onTouch(View view, MotionEvent event) {
        // Comme l'évènement nous donne la vue concernée par le toucher, on le récupère et on le caste en Button
        Button bouton = (Button)view;

        // On récupère la largeur du bouton
        int largeur = bouton.getWidth();
        // On récupère la hauteur du bouton
        int hauteur = bouton.getHeight();

        // On récupère la coordonnée sur l'abscisse (X) de l'évènement
        float x = event.getX();
        // On récupère la coordonnée sur l'ordonnée (Y) de l'évènement
        float y = event.getY();

        // Puis on change la taille du texte selon la formule indiquée dans l'énoncé
        bouton.setTextSize(Math.abs(x - largeur / 2) + Math.abs(y - hauteur / 2));
        // Le toucher est fini, on veut continuer à détecter les touchers d'après
        return true;
    }
}
