package com.example.stockex;

import android.os.Bundle;
import android.app.Activity;
import android.view.Menu;
import android.widget.ArrayAdapter;
import android.widget.ListView;

//import for reading json from django database
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.URI;

import org.apache.http.HttpEntity;
import org.apache.http.HttpResponse;
import org.apache.http.StatusLine;
import org.apache.http.client.ClientProtocolException;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.DefaultHttpClient;
import org.apache.http.util.EntityUtils;
import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import android.app.Activity;
import android.os.Bundle;
import android.util.Log;

public class StockEx extends Activity {

	@Override
	public void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_stock_ex);
		// String rStockExFeed = readStockExFeed();
		

		ListView companyA = (ListView) findViewById(R.id.GCB);

		

		// connecting to the database
		try {
			HttpClient client = new DefaultHttpClient(); 
			HttpGet request = new HttpGet();
			request.setURI(new URI("http://10.0.2.2:8000/Stock/json/companies/"));

			// next line throws exception
			HttpResponse response = client.execute(request);
			HttpEntity resEntity = response.getEntity();
			if (resEntity != null) {
				//Log.i("GET RESPONSE", EntityUtils.toString(resEntity));
				String jsonString = EntityUtils.toString(resEntity);
				//System.out.print(jsonString);
				Log.i("GET RESPONSE", jsonString);
				
				
				try{
				
				
				JSONObject jsonObj = new JSONObject(jsonString);
				JSONArray Companies = jsonObj.getJSONArray("companies");
				String[] Company_Name = new String[Companies.length()];
				String[] Conpany_Index = new String[Companies.length()];
				
				for (int i = 0; i < Companies.length(); i++ ){
					
					JSONObject company =Companies.getJSONObject(i);
					String index = company.getString("companyIndex");
					String name = company.getString("companyName");
					
					Company_Name [i] = name;
					Conpany_Index[i] = index;
					
				}
				
				companyA.setAdapter(new ArrayAdapter<String>(this,
						android.R.layout.simple_list_item_1, Company_Name));
				
				
				//String index=Companies.getJSONObject(0).getString("companyIndex");
				
				//System.out.print(index);
				//Log.i("This is index", index);
				}
				catch (JSONException e){
					
					e.printStackTrace();
					
					System.out.print("blaaasaf;hajkwefkenklfmjkwel");
				}
				//System.out.print(Companies.length());
				
				
				//for (int i = 0)
				// return jsonToAccount(jsonString);// create a method to dump
				// the json code
			}
		} catch (Exception e) {
			e.printStackTrace();
		}

	}

	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		getMenuInflater().inflate(R.menu.activity_stock_ex, menu);
		return true;
	}
}
