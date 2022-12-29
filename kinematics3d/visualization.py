""" Plotting and animation. """
import pickle
import numpy as np
import logging
import matplotlib.pyplot as plt
from matplotlib import animation
import mpl_toolkits.mplot3d.axes3d as p3
from mycolorpy import colorlist as mcp

# Change the logging level here
logging.basicConfig(
    level=logging.INFO,
    format=' %(asctime)s - %(levelname)s- %(message)s')


def plot_3d_points(points3d, key_points, t=0, **kwargs):
    """ Plots 3D points."""
    azim = kwargs.get('azim',90)#-21)
    elev = kwargs.get('elev',0)# 20)
    format_img = kwargs.get('format_img', 'png')
    export_path = kwargs.get('export_path', None)

    fig = plt.figure(figsize=(5, 5))
    ax3d = p3.Axes3D(fig)
    ax3d.view_init(azim=azim, elev=elev)

    # color_map_right = mcp.gen_color(cmap="RdPu", n=len(key_points))
    # color_map_left = mcp.gen_color(cmap="BuGn", n=len(key_points))
    color_map_scatter = mcp.gen_color(cmap="RdBu", n=len(key_points))

    i = 0
    for kp, (order, ls) in key_points.items():
        if len(order) > 3:
            ax3d.plot(
                points3d[t, order, 0],
                points3d[t, order, 1],
                points3d[t, order, 2],
                label=kp,
                linestyle=ls,
                linewidth=3,
                color=color_map_scatter[i]

            )
        else:
            ax3d.plot(
                points3d[t, order, 0],
                points3d[t, order, 1],
                points3d[t, order, 2],
                lw=2.5,
                label=kp,
                marker=ls,
                markersize=9,
                color=color_map_scatter[i]
            )
        i += 1

    # Setting the axes properties
    # try:
    #     ax3d.set_xlim3d([np.amin(points3d[...,0]), np.amax(points3d[...,0])])
    # except ValueError:
    #     ax3d.set_xlim3d([-82,82])
    # try:
    #     ax3d.set_ylim3d([np.amin(points3d[...,1]), np.amax(points3d[...,1])])
    # except ValueError:
    #     ax3d.set_ylim3d([-82,82])    # ax3d.set_xlim3d([-0.8,1.2])

    # try:
    #     ax3d.set_zlim3d([np.amin(points3d[...,2]), np.amax(points3d[...,2])])
    # except ValueError:
    #     ax3d.set_zlim3d([-82,82])
    # ax3d.set_xlim3d([-0.8,1.2])
    # ax3d.set_ylim3d([-.2,.2]) # ax3d.set_ylim3d([-1.0,1.0])
    # ax3d.set_zlim3d([-0.2,0.1])

    # ax3d.set_xticks([])
    # ax3d.set_yticks([])
    # ax3d.set_zticks([])
    # ax3d.invert_zaxis()

    ax3d.set_xlabel('x')
    ax3d.set_ylabel('y')
    ax3d.set_zlabel('z')

    # ax3d.set_title('DLC and DF3D Results')
    ax3d.legend(ncol=2, frameon=False)

    if export_path is not None:
        fig.savefig(export_path, bbox_inches='tight', format=format_img)

    plt.show()


def animate_3d_points(points3d, key_points, export_path, fps=100, frame_no=1000, format_video='mp4', **kwargs):
    """ Makes an animation from 3D plot."""
    azim = kwargs.get('azim',0)#-21)
    elev = kwargs.get('elev',10)# 20)
    fig = plt.figure()
    ax3d = p3.Axes3D(fig)
    ax3d.view_init(azim=azim, elev=elev)

    # color_map_right = mcp.gen_color(cmap="RdPu", n=len(key_points) + 3)
    # color_map_left = mcp.gen_color(cmap="BuGn", n=len(key_points) + 3)
    color_map_scatter = mcp.gen_color(cmap="RdBu", n=len(key_points))

    i = 0
    line_data = []

    for kp, (order, ls) in key_points.items():
        if len(order) > 3:
            line_data.append(ax3d.plot(
                points3d[0, order, 0],
                points3d[0, order, 1],
                points3d[0, order, 2],
                label=kp,
                linestyle=ls,
                linewidth=3,
                color=color_map_scatter[i]
            )[0]
            )
        else:
            line_data.append(ax3d.plot(
                points3d[0, order, 0],
                points3d[0, order, 1],
                points3d[0, order, 2],
                lw=2.5,
                label=kp,
                marker=ls,
                markersize=9,
                color=color_map_scatter[i],
                alpha=0.7
            )[0]
            )
        i += 1

    # Setting the axes properties
    # ax3d.set_xlim3d([-1,1])
    # ax3d.set_ylim3d([-1,1])
    # ax3d.set_zlim3d([-2,0.1])

    # ax3d.set_xticks([])
    # ax3d.set_yticks([])
    # ax3d.set_zticks([])

    #ax3d.set_title('DLC and DF3D Results')
    # ax3d.legend(bbox_to_anchor=(1.2, 0.9), frameon=False)

    def update(frame, lines, key_points):
        i = 0
        for kp, (kp_range, _) in key_points.items():
            lines[i].set_data(points3d[frame, kp_range, 0], points3d[frame, kp_range, 1])
            lines[i].set_3d_properties(points3d[frame, kp_range, 2])
            i += 1

    # Creating the Animation object
    line_ani = animation.FuncAnimation(fig, update, frame_no, fargs=(line_data, key_points),
                                       interval=10, blit=False)
    logging.info('Making animation...')
    export_path += f'.{format_video}' if not export_path.endswith(('.mp4', '.avi', '.mov')) else ''
    line_ani.save(export_path, fps=fps, dpi=300)
    logging.info(f'Animation is saved at {export_path}')
