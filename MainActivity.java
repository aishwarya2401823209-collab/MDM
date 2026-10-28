import android.os.Bundle;
import android.widget.*;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle b) {
        super.onCreate(b);

        LinearLayout l = new LinearLayout(this);
        l.setOrientation(1);

        EditText a = new EditText(this);
        a.setHint("First number");
        l.addView(a);

        EditText c = new EditText(this);
        c.setHint("Second number");
        l.addView(c);

        TextView result = new TextView(this);
        l.addView(result);

        Button btn = new Button(this);
        btn.setText("Add");
        l.addView(btn);

        btn.setOnClickListener(v -> {
            double x = Double.parseDouble(a.getText().toString());
            double y = Double.parseDouble(c.getText().toString());
            result.setText("Result: " + (x + y));
        });

        setContentView(l);
    }
}