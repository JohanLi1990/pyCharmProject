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
package org.eclipse.articles.adapters.properties;

import org.eclipse.articles.adapters.core.Person;
import org.eclipse.ui.views.properties.IPropertyDescriptor;
import org.eclipse.ui.views.properties.IPropertySource;
import org.eclipse.ui.views.properties.TextPropertyDescriptor;

public class PersonPropertySource implements IPropertySource {
	private final Person person;

	public PersonPropertySource(Person person) {
		this.person = person;
	}

	public Object getEditableValue() {
		return this;
	}

	public IPropertyDescriptor[] getPropertyDescriptors() {
		return new IPropertyDescriptor[] {
				new TextPropertyDescriptor("name", "Name"),
				new TextPropertyDescriptor("street", "Street"),
				new TextPropertyDescriptor("city", "City")
		};
	}

	public Object getPropertyValue(Object id) {
		if ("name".equals(id)) return person.getName();
		else if ("street".equals(id)) return person.getStreet();
		else if ("city".equals(id)) return person.getCity();
		return null;
	}

	public boolean isPropertySet(Object id) {
		return false;
	}

	public void resetPropertyValue(Object id) {
	}

	public void setPropertyValue(Object id, Object value) {
		if ("name".equals(id)) person.setName((String)value);
		else if ("street".equals(id)) person.setStreet((String)value);
		else if ("city".equals(id)) person.setCity((String)value);
	}

}