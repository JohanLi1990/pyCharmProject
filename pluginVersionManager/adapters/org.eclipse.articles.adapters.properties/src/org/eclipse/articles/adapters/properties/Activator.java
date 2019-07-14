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

import org.eclipse.core.runtime.IAdapterManager;
import org.eclipse.ui.IStartup;
import org.eclipse.ui.plugin.AbstractUIPlugin;

/**
 * This activator exists to force our adapter factory to work. The Properties
 * view uses the {@link IAdapterManager#getAdapter(Object, Class)} method which
 * only finds the adapter if the bundle that defines it has already been
 * activated. To make sure that our bundle is activated before we need it, it
 * defines an extension to <code>org.eclipse.ui.startup</code> which tells the
 * workbench to start this bundle when it starts.
 */
public class Activator extends AbstractUIPlugin implements IStartup {

	/**
	 * We don't actually need to do anything when we start. We just need this
	 * bundle to be activated so that the
	 * <code>org.eclipse.core.runtime.adapters</code> will work.
	 */
	public void earlyStartup() {

	}

}
