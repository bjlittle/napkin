#!/usr/bin/env python
"""
Provides "diff-like" comparison of images.

Currently relies on matplotlib for image processing so limited to PNG format.

"""

from __future__ import (absolute_import, division, print_function)

import os.path
import shutil
import sys

import matplotlib.pyplot as plt
import matplotlib.image as mimg
import matplotlib.widgets as mwidget

from napkin.tests import ImageTesting


def diff_viewer(expected_fname, result_fname, diff_fname):
    plt.figure(figsize=(16, 16))
    plt.suptitle(os.path.basename(expected_fname))
    ax = plt.subplot(221)
    ax.imshow(mimg.imread(expected_fname))
    ax = plt.subplot(222, sharex=ax, sharey=ax)
    ax.imshow(mimg.imread(result_fname))
    ax = plt.subplot(223, sharex=ax, sharey=ax)
    ax.imshow(mimg.imread(diff_fname))

    def accept(event):
        # removes the expected result, and move the most recent result in
        print('ACCEPTED NEW FILE: %s' % (os.path.basename(expected_fname), ))
        os.remove(expected_fname)
        shutil.copy2(result_fname, expected_fname)
        os.remove(diff_fname)
        plt.close()

    def reject(event):
        print('REJECTED: %s' % (os.path.basename(expected_fname), ))
        plt.close()

    ax_accept = plt.axes([0.7, 0.05, 0.1, 0.075])
    ax_reject = plt.axes([0.81, 0.05, 0.1, 0.075])
    bnext = mwidget.Button(ax_accept, 'Accept change')
    bnext.on_clicked(accept)
    bprev = mwidget.Button(ax_reject, 'Reject')
    bprev.on_clicked(reject)

    plt.show()


def step_over_diffs():
    image_dir = os.path.join(ImageTesting.root_image_results,
                             'baseline_images', 'mpl')
    diff_dir = os.path.join(ImageTesting.image_output_directory)

    for test_dname in sorted(os.listdir(image_dir)):
        dname = os.path.join(image_dir, test_dname)
        for image_fname in sorted(os.listdir(dname)):
            result_path = os.path.join(diff_dir, test_dname,
                                       'result-{}'.format(image_fname))
            diff_path = result_path[:-4] + '-failed-diff.png'

            # If the test failed, there will be a diff file.
            if os.path.exists(diff_path):
                expected_path = os.path.join(dname, image_fname)
                diff_viewer(expected_path, result_path, diff_path)


if __name__ == '__main__':
    # Force iris.tests to use the ```tkagg``` backend by using the '-d'
    # command-line argument as idiff is an interactive tool that requires a
    # gui interface.
    sys.argv.append('-d')

    step_over_diffs()
