package com.proxydeal;

import java.util.Map;

import redis.clients.jedis.Jedis;

/**
 * 
 * @date 2015年1月8日
 * @author cutoutsy
 * @function fiter proxy when the error number greater than 10000 
 *
 */
public class ProxyFilter {
	
	private static  Jedis redis;
	 static Map<String,String> proxy_err;
	
	public static void fiterProxy(int sum,int error){
//		redis = new Jedis("127.0.0.1",6379,10000);
		redis = new Jedis("192.168.1.211",6379,10000);
		redis.auth("xidian123");
		
		proxy_err = redis.hgetAll("ip_port");
		if(proxy_err.size() > sum ){
		for(Map.Entry entry: proxy_err.entrySet()) {   
//             System.out.print(entry.getKey() + ":" + entry.getValue() + "\t");
			int errorNum = Integer.valueOf(entry.getValue().toString());
			if(errorNum >= error){
				redis.hdel("ip_port", entry.getKey().toString());
			}
        }
		}
	}
}
