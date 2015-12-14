package com.mobiserenity.formationandroid;

import android.app.Activity;
import android.os.AsyncTask;
import android.os.Bundle;
import android.widget.ProgressBar;
import android.widget.TextView;
import android.widget.Toast;

import java.util.Random;
import java.util.concurrent.Semaphore;

/**
 * Created by Luc Maignan on 01/09/2015.
 */
public class Philo extends Activity {

    Semaphore semRepas;
    ProgressBar pb1, pb2, pb3, pb4, pb5;
    int nbPhilo = 0;

    public void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);
        setContentView(R.layout.philo);
        pb1 = (ProgressBar) findViewById(R.id.pbPhilo1);
        pb2 = (ProgressBar) findViewById(R.id.pbPhilo2);
        pb3 = (ProgressBar) findViewById(R.id.pbPhilo3);
        pb4 = (ProgressBar) findViewById(R.id.pbPhilo4);
        pb5 = (ProgressBar) findViewById(R.id.pbPhilo5);

        semRepas = new Semaphore(1);

        Philosophe socrate = new Philosophe(1,"Socrate");
        Philosophe platon = new Philosophe(2, "Platon");
        Philosophe pascal = new Philosophe(3, "Pascal");
        Philosophe kant = new Philosophe(4, "Kant");
        Philosophe spinoza = new Philosophe(5, "Spinoza");


        Philosophe[] lp = {socrate, platon, pascal, kant, spinoza};

        for ( int i = 0; i < lp.length; i++)
            lp[i].executeOnExecutor(AsyncTask.THREAD_POOL_EXECUTOR);


        //finish();

    }

    private class Philosophe extends AsyncTask<Void, Integer, Void>
    {
        int nbRepas;
        int no;
        String name;
        private final int MAX_REPAS = 7;

        public Philosophe(int no,String name) {
            nbRepas = 0;
            this.no  = no;
            nbPhilo++;
            this.name = name;
        }

        @Override
        protected void onPreExecute ( ) {

            TextView txName = null;
            switch (no)
            {
                case 1: txName = (TextView)findViewById(R.id.txPhilo1);
                        break;
                case 2: txName = (TextView)findViewById(R.id.txPhilo2);
                        break;
                case 3: txName = (TextView)findViewById(R.id.txPhilo3);
                        break;
                case 4: txName = (TextView)findViewById(R.id.txPhilo4);
                        break;
                case 5: txName = (TextView)findViewById(R.id.txPhilo5);
                        break;
            }

            txName.setText(name);
        }
        @Override
        protected Void doInBackground(Void... arg0){

            Random rand = new Random();

            while ( nbRepas <= MAX_REPAS) {
                publishProgress(nbRepas);

                if (semRepas.tryAcquire() == true) {
                    nbRepas++;
                    semRepas.release();
                    try {
                        // thread to sleep for 1000 milliseconds

                        Thread.sleep(rand.nextInt(4000));
                    } catch (Exception e) {
                        System.out.println(e);
                        }
                }
                }

            return null;

        }

        @Override
        protected void onProgressUpdate(Integer... values) {
            super.onProgressUpdate(values);
            // Mise à jour de la ProgressBar
            ProgressBar pb = null;

            switch (no)
            {
                case 1 : pb = pb1;
                         break;
                case 2 : pb = pb2;
                         break;
                case 3 : pb = pb3;
                    break;
                case 4 : pb = pb4;
                    break;
                case 5 : pb = pb5;
                    break;
            }

            pb.setProgress(values[0]);
        }

        @Override
        protected  void onPostExecute ( Void result ){
            nbPhilo--;

            if ( nbPhilo == 0)
            {
                Toast.makeText(Philo.this, "Les philosophes se retirent...", Toast.LENGTH_LONG).show();
                finish();
            }
        }


    }

}
