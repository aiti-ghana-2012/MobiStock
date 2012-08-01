package com.example.stockex;


import com.example.stockex.R;
import android.os.Bundle;
import android.provider.ContactsContract;
import android.app.Activity;
import android.app.ExpandableListActivity;
import android.view.Menu;
import android.widget.ArrayAdapter;
import android.widget.ExpandableListView;
import android.widget.ExpandableListView.OnGroupExpandListener;
import android.widget.ListView;
import android.widget.SimpleExpandableListAdapter;

//import for reading json from django database
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.URI;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;

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

//import android.app.Activity;
//import android.os.Bundle;
import android.support.v4.widget.SimpleCursorAdapter;
import android.util.Log;

public class StockEx extends ExpandableListActivity {

	@Override
	public void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_stock_ex);
		
		
		
													
									
		
		//ListView companyA = (ListView) findViewById(R.id.GCB);

	
		// connecting to the database
		try {
			HttpClient client = new DefaultHttpClient(); 
			HttpGet request1 = new HttpGet();
			HttpGet request2 = new HttpGet();
			
			request1.setURI(new URI("http://10.0.2.2:8000/Stock/json/companies/")); //connection to local machine
			request2.setURI(new URI("http://10.0.2.2:8000/Stock/json/index/"));
			
			// next line throws exception
			HttpResponse response = client.execute(request1);
			HttpResponse response2 = client.execute(request2);
			
			HttpEntity resEntity = response.getEntity();
			HttpEntity resEntity2 = response2.getEntity();
			if (resEntity2 != null) {
				//Log.i("GET RESPONSE", EntityUtils.toString(resEntity));
				String jsonString = EntityUtils.toString(resEntity);
				String jsonString2 = EntityUtils.toString(resEntity2);
				//System.out.print(jsonString);
				Log.i("GET COMPANIES", jsonString);
				Log.i("GET INDEX", jsonString2);
				
				try {
					
				JSONObject jsonObj = new JSONObject(jsonString);
				JSONObject jsonObj2 = new JSONObject(jsonString2);
				JSONArray Companies = jsonObj.getJSONArray("companies");
				JSONArray Index = jsonObj2.getJSONArray("assets");
				
				
				String[][] Company_Name = new String[Index.length()][5];
				String[] Conpany_Index = new String[Companies.length()];
				String [] Parent =  new String[Companies.length()];
				String [][] Children =  new String[Companies.length()][3];
				
				//String[] Asset_Name = new String[Index.length()];
				//String[] Volume_traded = new String[Index.length()];
				
				for (int i = 0; i < Index.length(); i++ ){
										
					JSONObject company =Companies.getJSONObject(i);
					String index = company.getString("companyIndex");
					String company_Name = company.getString("companyName");
					
					JSONObject in_dex = Index.getJSONObject(i);
					//JSONObject volumeTraded = Index.getJSONObject(i);
					String indexName = in_dex.getString("index_Name");
					String volTrad = in_dex.getString("volume_traded");
					String price_per_share = in_dex.getString("price_per_share");
					String  price_change_per_share = in_dex.getString("price_change_per_share");
					String dd = "";
					//Asset_Name [i] = assetName;
					
			        Parent[i] = company_Name;
					Children[i][0] = volTrad;
					Children[i][1] = price_per_share;
					Children[i][2] = price_change_per_share;
					Company_Name [i][0] = company_Name;
					Company_Name [i][1] = indexName;
					Company_Name [i][2] = volTrad;
					Company_Name [i][3] = price_per_share;
					Company_Name [i][4] = price_change_per_share;
					
					//Conpany_Index[i] = index;
					
				}
				
				SimpleExpandableListAdapter companyAdapter = new SimpleExpandableListAdapter (this,
						                                     createGroupList(Parent),
						                                     R.layout.child_row,
						                                     new String [] {"company_Name"},
						                                     new int []{R.id.childname},
						                                     createChildList(Children),
						                                     R.layout.child_row,
						                                     new String []{"company_Info"},
						                                     new int []{R.id.childname});
				
				ExpandableListView expList =getExpandableListView();
				expList.setAdapter(companyAdapter);
				expList.setOnGroupExpandListener(new OnGroupExpandListener()
				{    @Override
					
					public void onGroupExpand(int groupPosition)
					{
						 
						Log.e("onGroupExpand","ok");
						
					}
				});
				
				
				//setListAdapter(companyAdapter);
						 
				
				//companyA.setAdapter(new ArrayAdapter<String>(this, android.R.layout.simple_expandable_list_item_1, Company_Name[i]));
                //ArrayList 
				//for (int c=0; c< Index.length(); c++){

					//neComp = Arrays.toString(Company_Name[c]) +" | "+ Arrays.toString(Company_Name[c+1]) ;
				
				//companyA.setAdapter(new ArrayAdapter<String>(this,
					//	android.R.layout.simple_list_item_1, Asset_Name));
				
				//String[] fromColumns = {ContactsContract.Data.DISPLAY_NAME, 
                   //     ContactsContract.CommonDataKinds.Phone.NUMBER};
				//int[] toViews = {R.id.CompanyName, R.id.PriceChangePerShare,R.id.PriceChangePerShare,R.id.VolumeTraded};
				
		      //System.out.println(neComp);}
				//companyA.setAdapter(new ArrayAdapter<String>(this, android.R.layout.simple_expandable_list_item_1, Company_Name[0]));
				//companyA.setAdapter(new ArrayAdapter<String>(this, android.R.layout.simple_list_item_1, Company_Name[1]));
				
				//SimpleCursorAdapter adapter = new SimpleCursorAdapter(this, 
				  //      R.layout.activity_stock_ex, Company_Name[0], Company_Name[1], toViews, 0);
				
				//String index=Companies.getJSONObject(0).getString("companyIndex");
				
				//System.out.print(index);
				//Log.i("This is index", index);
				}
				catch (JSONException e){
					
					e.printStackTrace();
					
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
	//new fu
	private List createGroupList(String[] a){
		ArrayList result = new ArrayList();
		for(int m = 0; m < a.length; m++){
			HashMap<String, String> i = new HashMap<String, String>();
			i.put("company_Name",a[m]);	
			result.add (i);
		}return (List)result;
		}
	private List createChildList(String[][] a){
		ArrayList result = new ArrayList();
		for(int i = 0; i < a.length; i++){
			ArrayList secList = new ArrayList();
			for(int n = 0; n < a[i].length; n++){
				HashMap<String, String> child = new HashMap<String, String>();
			child.put("company_Info",a[i][n]);
			}
			result.add (secList);
		}
		return result;
		}
	
	
	
}
