/*******************************************************************************
 * Copyright (c) 2008 The Eclipse Foundation.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * which accompanies this distribution, and is available at
 * http://www.eclipse.org/legal/epl-v10.html
 * 
 * Contributors:
 *    The Eclipse Foundation - initial API and implementation
 *******************************************************************************/
package org.eclipse.articles.adapters.core;

public class Person {
	private String name;
	private Object street;
	private Object city;

	public Person(String name) {
		this.setName(name);
		this.setStreet("");
		this.setCity("");
	}

	public void setName(String name) {
		this.name = name;
	}

	public String getName() {
		return name;
	}

	public void setStreet(Object street) {
		this.street = street;
	}

	public Object getStreet() {
		return street;
	}

	public void setCity(Object city) {
		this.city = city;
	}

	public Object getCity() {
		return city;
	}

}