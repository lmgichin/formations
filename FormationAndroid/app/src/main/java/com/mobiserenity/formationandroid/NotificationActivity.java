package com.mobiserenity.formationandroid;

import android.app.Activity;
import android.app.Notification;
import android.app.NotificationManager;
import android.app.PendingIntent;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

/**
 * Created by lucio on 27/08/15.
 */
public class NotificationActivity extends Activity {

    private int notificationId = 1;
    private int REQUEST_CODE = 10;

    public void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);
        setContentView(R.layout.act_notification);

        Button addNotificationBtn = (Button) findViewById(R.id.addNotification);

        addNotificationBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                createSimpleNotification();
            }
        });
    }

    protected void createSimpleNotification() {
        final NotificationManager notificationManager = (NotificationManager) getSystemService(NOTIFICATION_SERVICE);
        final Intent notificationIntent = new Intent(this,NotificationActivity.class);

        final PendingIntent notificationPendingIntent =
                PendingIntent.getActivity(this, REQUEST_CODE, notificationIntent, PendingIntent.FLAG_ONE_SHOT);

        Notification.Builder notificationBuilder =
                new Notification.Builder(this)
                        .setWhen(System.currentTimeMillis())
                        .setTicker(getResources().getString(
                                R.string.notification_launching_title))
                        .setSmallIcon(R.mipmap.ic_launcher)
                        .setContentTitle(
                                getResources().getString(R.string.notification_title))
                        .setContentText(getResources().getString(R.string.notification_desc))
                        .setContentIntent(notificationPendingIntent);

        PendingIntent pIntent = PendingIntent.getActivity(this, (int) System.currentTimeMillis(), notificationIntent, 0);
        notificationBuilder.addAction(R.mipmap.ic_launcher, getString(R.string.share), pIntent);

        notificationManager.notify(notificationId, notificationBuilder.getNotification());
    }
}
