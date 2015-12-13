package com.mobiserenity.formationandroid;

import android.app.Activity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TableLayout;
import android.widget.TableRow;
import android.widget.TextView;

/**
 * Created by Luc Maignan on 12/08/2015.
 */
public class TicTacToeActivity extends Activity {

    private boolean noughtsTurn = false; // Who's turn is it? false=X true=O
    private char board[][] = new char[3][3]; // for now we will represent the board as an array of characters

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.tictactoe);
        setupOnClickListeners();
    }

    private void setupOnClickListeners() {
        TableLayout T = (TableLayout) findViewById(R.id.tableLayout);
        for(int y = 0; y < T.getChildCount(); y ++) {
            if(T.getChildAt(y) instanceof TableRow) {
                TableRow R = (TableRow) T.getChildAt(y);
                for(int x = 0; x < R.getChildCount(); x ++) {
                    View V = R.getChildAt(x); // In our case this will be each button on the grid
                    V.setOnClickListener(new PlayOnClick(x, y));
                }
            }
        }
    }

    private class PlayOnClick implements View.OnClickListener {

        private int x = 0;
        private int y = 0;

        public PlayOnClick(int x, int y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public void onClick(View view) {
            if(view instanceof Button) {
                Button B = (Button) view;
                board[x][y] =  noughtsTurn ? 'O' : 'X';
                B.setText(noughtsTurn ? "O" : "X");
                B.setTextColor(getResources().getColor(noughtsTurn ? R.color.rouge : R.color.vert));
                B.setEnabled(false);
                noughtsTurn = !noughtsTurn;

                // check if anyone has won
                if (checkWin()) {
                    resetButtons(false);
                }

            }
        }
    }

    public void newGame(View view) {
        noughtsTurn = false;
        board = new char[3][3];
        resetButtons(true);

        TextView T = (TextView) findViewById(R.id.textView);
        T.setText(getResources().getString(R.string.titre_ttt));

    }

    /**
     * Reset each button in the grid to be blank and enabled.
     */
    private void resetButtons(boolean disable) {
        TableLayout T = (TableLayout) findViewById(R.id.tableLayout);
        for (int y = 0; y < T.getChildCount(); y++) {
            if (T.getChildAt(y) instanceof TableRow) {
                TableRow R = (TableRow) T.getChildAt(y);
                for (int x = 0; x < R.getChildCount(); x++) {
                    if(R.getChildAt(x) instanceof Button) {
                        Button B = (Button) R.getChildAt(x);

                        if (disable)
                            B.setText("");

                        B.setEnabled(disable);
                    }
                }
            }
        }
    }

    private boolean checkWinner(char[][] board, int size, char player) {
        // check each column
        for (int x = 0; x < size; x++) {
            int total = 0;
            for (int y = 0; y < size; y++) {
                if (board[x][y] == player) {
                    total++;
                }
            }
            if (total >= size) {
                return true; // they win
            }
        }

        // check each row
        for (int y = 0; y < size; y++) {
            int total = 0;
            for (int x = 0; x < size; x++) {
                if (board[x][y] == player) {
                    total++;
                }
            }
            if (total >= size) {
                return true; // they win
            }
        }

        // forward diag
        int total = 0;
        for (int x = 0; x < size; x++) {
            for (int y = 0; y < size; y++) {
                if (x == y && board[x][y] == player) {
                    total++;
                }
            }
        }
        if (total >= size) {
            return true; // they win
        }

        // backward diag
        total = 0;
        for (int x = 0; x < size; x++) {
            for (int y = 0; y < size; y++) {
                if (x + y == size - 1 && board[x][y] == player) {
                    total++;
                }
            }
        }
        if (total >= size) {
            return true; // they win
        }

        return false; // nobody won
    }

    private boolean checkWin() {

        char winner = '\0';
        if (checkWinner(board, 3, 'X')) {
            winner = 'X';
        } else if (checkWinner(board, 3, 'O')) {
            winner = 'O';
        }

        if (winner == '\0') {
            return false; // nobody won
        } else {
            // display winner
            TextView T = (TextView) findViewById(R.id.textView);
            T.setText(winner + " wins");
            return true;
        }
    }






}
