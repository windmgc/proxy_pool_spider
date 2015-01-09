package com.proxydeal;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

import redis.clients.jedis.Jedis;

/**
 * 
 * @date 2015年1月8日
 * @author cutoutsy
 * @function import proxy from text to redis
 *
 */
public class ProxyToRedis {
	private static  Jedis redis;
	private static  FileReader fileReader;
	
	
	//import sucess return true;else return false
	
	public static boolean importProxy(String path){
		boolean flag = true;
		
//		redis = new Jedis("127.0.0.1",6379,10000);
		redis = new Jedis("192.168.1.211",6379,10000);
		redis.auth("xidian123");
		
		try {
			fileReader =new FileReader(path);
		} catch (FileNotFoundException e) {
			e.printStackTrace();
			flag = false;
		}
		BufferedReader reader = new BufferedReader(fileReader);
		String str;
		
		try {
			while((str = reader.readLine()) != null){
				redis.hset("ip_port", str, "0");
			}
		} catch (IOException e) {
			e.printStackTrace();
			flag = false;
		}
		
		return flag;
	}
	
	
}
