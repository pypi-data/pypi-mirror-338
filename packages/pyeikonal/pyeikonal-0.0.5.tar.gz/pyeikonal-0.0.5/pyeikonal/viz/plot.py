import numpy as np
import plotly.colors as pc
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.ticker import MaxNLocator


def _get_cmap(cmap):
    """Return a color map from a colormap or string."""
    if isinstance(cmap, str):  # get color map if a string was passed
        cmap = plt.get_cmap(cmap)
    return cmap


def _get_ax(ax, figsize=None, **kwargs):
    """Get an axis if ax is None"""
    if ax is None:
        _, ax = plt.subplots(1, 1, figsize=figsize, **kwargs)
    return ax


def plot_model2d(
    nx,
    nz,
    dx,
    dz,
    model=None,
    mask=None,
    colorbar=True,
    cmap="jet_r",
    alpha=1,
    tt=None,
    contour_levels=None,
    contour_colors="black",
    contour_alpha=0.5,
    contour_linewidths=0.2,
    contour_linestyles="-",
    source=None,
    source_marker="*",
    source_color="red",
    source_alpha=1,
    source_size=50,
    receiver=None,
    receiver_marker="^",
    receiver_color="deepskyblue",
    receiver_alpha=1,
    receiver_size=30,
    invert_x=False,
    invert_y=False,
    xlim=[None, None],
    ylim=[None, None],
    clip=[None, None],
    ax=None,
    figsize=(10, 5),
    show=True,
    save_path=None,
    dpi=100,
):

    ax = _get_ax(ax, figsize=figsize)
    xmax = nx * dx
    zmax = nz * dz

    if tt is not None:
        if contour_levels is None:
            contour_levels = np.linspace(tt.min(), tt.max(), 5)
        ax.contour(
            tt.T,
            levels=contour_levels,
            colors=contour_colors,
            alpha=contour_alpha,
            linewidths=contour_linewidths,
            linestyles=contour_linestyles,
            extent=[0, xmax, 0, zmax],
        )

    if model is not None:
        if mask is not None:
            model = np.ma.masked_where(mask == 0, model)
        im = ax.imshow(
            model.T,
            cmap=cmap,
            alpha=alpha,
            extent=[0, xmax, zmax, 0],
            origin="upper",
            aspect="auto",
        )
        if clip[0] is not None and clip[1] is not None:
            im.set_clim(clip[0], clip[1])
        if colorbar:
            plt.colorbar(im, orientation="vertical", ax=ax, label="Velocity (m/s)")

    if source is not None:
        ax.scatter(
            source[:, 0],
            source[:, 1],
            marker=source_marker,
            s=source_size,
            color=source_color,
            alpha=source_alpha,
        )

    if receiver is not None:
        ax.scatter(
            receiver[:, 0],
            receiver[:, 1],
            marker=receiver_marker,
            s=receiver_size,
            color=receiver_color,
            alpha=receiver_alpha,
        )

    if xlim[0] is not None and xlim[1] is not None:
        ax.set_xlim(xlim)
    if ylim[0] is not None and ylim[1] is not None:
        ax.set_ylim(ylim)

    ax.set_xlabel("X (m)")
    ax.set_ylabel("Z (m)")

    if invert_x:
        ax.invert_xaxis()

    if invert_y:
        ax.invert_yaxis()

    if show:
        plt.show()

    fig = ax.figure
    if save_path is not None:
        fig.savefig(save_path, dpi=dpi, bbox_inches="tight")
    else:
        return ax


def plot_model3d(
    nx,
    ny,
    nz,
    dx,
    dy,
    dz,
    source=None,
    receiver=None,
    xlim=[None, None],
    ylim=[None, None],
    zlim=[None, None],
    grid=True,
    box_aspect=[1, 1, 0.9],
    fig=None,
    legend=False,
    template="ggplot2",  # "plotly", "plotly_white", "plotly_dark", "ggplot2", "seaborn", "simple_white", "none"
    pane_color=None,  # "white",
    width=900,
    height=700,
    show=True,
    save_path=None,
):
    if fig is None:
        fig = go.Figure()

    if source is not None:
        for i in range(len(source)):
            fig.add_trace(
                go.Scatter3d(
                    x=[source[i][0]],
                    y=[source[i][1]],
                    z=[source[i][2]],
                    mode="markers",
                    marker=dict(color="red", size=5),
                    name=f"Source {i}",
                )
            )

    if receiver is not None:
        for i in range(len(receiver)):
            fig.add_trace(
                go.Scatter3d(
                    x=[receiver[i][0]],
                    y=[receiver[i][1]],
                    z=[receiver[i][2]],
                    mode="markers",
                    marker=dict(color="blue", size=3),
                    name=f"Receiver {i}",
                )
            )

    if xlim[0] is None or xlim[1] is None:
        xlim = [0, nx * dx]
    if ylim[0] is None or ylim[1] is None:
        ylim = [0, ny * dy]
    if zlim[0] is None or zlim[1] is None:
        zlim = [0, nz * dz]
        z_autorange = "reversed"
    else:
        zlim = [zlim[1], zlim[0]]
        z_autorange = None

    fig.update_layout(
        autosize=False,
        width=width,
        height=height,
        hovermode="closest",
        showlegend=legend,
        scene=dict(
            xaxis=dict(title="X (m)", range=xlim, showgrid=grid),
            yaxis=dict(title="Y (m)", range=ylim, showgrid=grid),
            zaxis=dict(
                title="Z (m)",
                range=zlim,
                autorange=z_autorange,
                showgrid=grid,
            ),
            aspectmode="manual",
            aspectratio=dict(x=box_aspect[0], y=box_aspect[1], z=box_aspect[2]),
            bgcolor=pane_color,
        ),
        template=template,
    )

    # show
    if show:
        fig.show()

    # save
    if save_path:
        fig.write_html(save_path)
    else:
        return fig


def plot_ray2d(
    ray,
    color="black",
    alpha=1,
    linewidth=0.6,
    linestyle="-",
    invert_x=False,
    invert_y=False,
    xlim=[None, None],
    ylim=[None, None],
    ax=None,
    figsize=(10, 5),
    show=True,
    save_path=None,
    dpi=100,
):
    ax = _get_ax(ax, figsize=figsize)

    for i in range(len(ray)):
        ax.plot(
            ray[i][:, 0],
            ray[i][:, 1],
            color=color,
            alpha=alpha,
            linewidth=linewidth,
            linestyle=linestyle,
        )

    ax.set_xlabel("X (m)")
    ax.set_ylabel("Z (m)")

    if xlim[0] is not None and xlim[1] is not None:
        ax.set_xlim(xlim)
    if ylim[0] is not None and ylim[1] is not None:
        ax.set_ylim(ylim)

    if invert_x:
        ax.invert_xaxis()

    if invert_y:
        ax.invert_yaxis()

    if show:
        plt.show()

    fig = ax.figure
    if save_path is not None:
        fig.savefig(save_path, dpi=dpi, bbox_inches="tight")
    else:
        return ax


def plot_ray3d(
    ray,
    linecolor="black",
    linewidth=0.6,
    linestyle="solid",
    xlim=[None, None],
    ylim=[None, None],
    zlim=[None, None],
    grid=True,
    box_aspect=[1, 1, 0.9],
    fig=None,
    legend=False,
    template="ggplot2",  # "plotly", "plotly_white", "plotly_dark", "ggplot2", "seaborn", "simple_white", "none"
    pane_color=None,  # "white",
    width=900,
    height=700,
    show=True,
    save_path=None,
):
    if fig is None:
        fig = go.Figure()

    if ray is not None:
        for i in range(len(ray)):
            x = ray[i][:, 0]
            y = ray[i][:, 1]
            z = ray[i][:, 2]
            fig.add_trace(
                go.Scatter3d(
                    x=x,
                    y=y,
                    z=z,
                    mode="lines",
                    line=dict(color=linecolor, width=linewidth, dash=linestyle),
                    name=f"Ray {i}",
                )
            )

    if zlim[0] is None or zlim[1] is None:
        zlim = None
        z_autorange = "reversed"
    else:
        zlim = [zlim[1], zlim[0]]
        z_autorange = None

    fig.update_layout(
        autosize=False,
        width=width,
        height=height,
        hovermode="closest",
        showlegend=legend,
        scene=dict(
            xaxis=dict(title="X (m)", range=xlim, showgrid=grid),
            yaxis=dict(title="Y (m)", range=ylim, showgrid=grid),
            zaxis=dict(
                title="Z (m)",
                range=zlim,
                autorange=z_autorange,
                showgrid=grid,
            ),
            aspectmode="manual",
            aspectratio=dict(x=box_aspect[0], y=box_aspect[1], z=box_aspect[2]),
            bgcolor=pane_color,
        ),
        template=template,
    )

    # show
    if show:
        fig.show()

    # save
    if save_path:
        fig.write_html(save_path)
    else:
        return fig


def plot_grad2d(
    nx,
    nz,
    dx,
    dz,
    grad,
    colorbar=True,
    cmap="seismic",
    alpha=1,
    invert_x=False,
    invert_y=False,
    xlim=[None, None],
    ylim=[None, None],
    clip=[None, None],
    ax=None,
    figsize=(10, 5),
    show=True,
    save_path=None,
    dpi=100,
):
    ax = _get_ax(ax, figsize=figsize)
    xmax = nx * dx
    zmax = nz * dz

    im = ax.imshow(
        grad.T,
        cmap=cmap,
        alpha=alpha,
        extent=[0, xmax, zmax, 0],
        origin="upper",
        aspect="auto",
    )

    ax.set_xlabel("X (m)")
    ax.set_ylabel("Z (m)")

    if clip[0] is not None and clip[1] is not None:
        im.set_clim(clip[0], clip[1])

    if colorbar:
        plt.colorbar(im, orientation="vertical", ax=ax, label="Gradient (m/s)")

    if xlim[0] is not None and xlim[1] is not None:
        ax.set_xlim(xlim)
    if ylim[0] is not None and ylim[1] is not None:
        ax.set_ylim(ylim)

    if invert_x:
        ax.invert_xaxis()

    if invert_y:
        ax.invert_yaxis()

    if show:
        plt.show()

    fig = ax.figure
    if save_path is not None:
        fig.savefig(save_path, dpi=dpi, bbox_inches="tight")
    else:
        return ax


def plot_grad3d(
    nx,
    ny,
    nz,
    dx,
    dy,
    dz,
    grad,
    threshold=0.0,
    xlim=[None, None],
    ylim=[None, None],
    zlim=[None, None],
    clip=[None, None],
    grid=True,
    box_aspect=[1, 1, 0.9],
    fig=None,
    legend=False,
    template="ggplot2",  # "plotly", "plotly_white", "plotly_dark", "ggplot2", "seaborn", "simple_white", "none"
    pane_color=None,  # "white",
    width=900,
    height=700,
    show=True,
    save_path=None,
):

    if fig is None:
        fig = go.Figure()

    if grad is not None:
        nz_mask = np.abs(grad) > threshold
        nz_indices = np.where(nz_mask)
        x, y, z = (
            nz_indices[0] * dx,
            nz_indices[1] * dy,
            nz_indices[2] * dz,
        )
        colors = grad[nz_mask]
        if clip[0] is None and clip[1] is None:
            color_max = np.max(np.abs(colors))
            cmin, cmax = -color_max, color_max
        else:
            cmin, cmax = clip

        fig.add_trace(
            go.Scatter3d(
                x=x,
                y=y,
                z=z,
                mode="markers",
                marker=dict(
                    color=colors,
                    colorscale=pc.diverging.RdBu,
                    cmin=cmin,
                    cmax=cmax,
                    size=3,
                    colorbar=dict(title="Gradient (m/s)"),
                ),
            )
        )

    if xlim[0] is None or xlim[1] is None:
        xlim = [0, nx * dx]
    if ylim[0] is None or ylim[1] is None:
        ylim = [0, ny * dy]
    if zlim[0] is None or zlim[1] is None:
        zlim = [0, nz * dz]
        z_autorange = "reversed"
    else:
        zlim = [zlim[1], zlim[0]]
        z_autorange = None

    fig.update_layout(
        autosize=False,
        width=width,
        height=height,
        hovermode="closest",
        showlegend=legend,
        scene=dict(
            xaxis=dict(title="X (m)", range=xlim, showgrid=grid),
            yaxis=dict(title="Y (m)", range=ylim, showgrid=grid),
            zaxis=dict(
                title="Z (m)",
                range=zlim,
                autorange=z_autorange,
                showgrid=grid,
            ),
            aspectmode="manual",
            aspectratio=dict(x=box_aspect[0], y=box_aspect[1], z=box_aspect[2]),
            bgcolor=pane_color,
        ),
        template=template,
    )

    # show
    if show:
        fig.show()

    # save
    if save_path:
        fig.write_html(save_path)
    else:
        return fig


def plot_animation2d(
    models,  # list
    dx,
    dz,
    colorbar=True,
    cmap="jet_r",
    alpha=1,
    ax=None,
    xlim=[None, None],
    ylim=[None, None],
    clip=[None, None],
    figsize=(10, 6),
    dpi=100,
):
    nx, nz = models[0].shape
    xmax = nx * dx
    zmax = nz * dz
    if xlim[0] is None and xlim[1] is None:
        xlim = [0, xmax]

    if ylim[0] is None and ylim[1] is None:
        ylim = [zmax, 0]
    else:
        ylim = [ylim[1], ylim[0]]

    if clip[0] is None and clip[1] is None:
        vmin = min(np.min(m) for m in models)
        vmax = max(np.max(m) for m in models)
    else:
        vmin = clip[0]
        vmax = clip[1]

    # plot static model
    ax = _get_ax(ax, figsize=figsize, dpi=dpi)
    fig = ax.figure
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    ax.set_xlabel("X (m)")
    ax.set_ylabel("Z (m)")

    # plot iter_model
    artists = []
    for i in range(0, len(models)):
        im = ax.imshow(
            models[i].T,
            cmap=cmap,
            alpha=alpha,
            vmin=vmin,
            vmax=vmax,
            extent=[0, xmax, zmax, 0],
            origin="upper",
            aspect="auto",
        )
        txt = ax.text(
            0.02,
            1.05,
            f"Iteration {i+1}",
            transform=ax.transAxes,
            fontsize=12,
            color="black",
            verticalalignment="top",
            animated=True,
        )
        artists.append([im, txt])

    if colorbar:
        plt.colorbar(
            artists[0][0], orientation="vertical", ax=ax, label="Velocity (m/s)"
        )

    ani = animation.ArtistAnimation(fig, artists, interval=200, blit=True)

    plt.close(fig)

    return ani


def plot_histogram(
    tt,
    tt0=None,
    nbins=30,
    xlim=[None, None],
    ylim=[None, None],
    facecolor=["red", "limegreen"],
    edgecolor="black",
    alpha=0.5,
    histtype="bar",  # "stepfilled",
    legend_loc="upper right",
    grid=True,
    ax=None,
    figsize=(6, 4),
    show=True,
    save_path=None,
    dpi=100,
):
    tt = np.array(tt).flatten()
    if tt0 is not None:
        tt0 = np.array(tt0).flatten()
        bins = np.linspace(
            min(np.min(tt), np.min(tt0)), max(np.max(tt), np.max(tt0)), nbins
        )
    else:
        bins = np.linspace(np.min(tt), np.max(tt), nbins)

    # histogram
    ax = _get_ax(ax, figsize=figsize)
    if tt0 is not None:
        ax.hist(
            tt0,
            bins=bins,
            facecolor=facecolor[0],
            edgecolor=edgecolor,
            alpha=alpha,
            histtype=histtype,
            label="Initial",
        )
        ax.hist(
            tt,
            bins=bins,
            facecolor=facecolor[1],
            edgecolor=edgecolor,
            alpha=alpha,
            histtype=histtype,
            label="Final",
        )
    else:
        ax.hist(
            tt,
            bins=bins,
            facecolor=facecolor[0],
            edgecolor=edgecolor,
            alpha=alpha,
            histtype=histtype,
            label="Final",
        )
    # axis limits
    if xlim[0] is not None and xlim[1] is not None:
        ax.set_xlim(xlim)
    if ylim[0] is not None and ylim[1] is not None:
        ax.set_ylim(ylim)

    # axis labels
    ax.set_xlabel("Residuals (s)")
    ax.set_ylabel("Counts")

    # legend, grid
    ax.legend(loc=legend_loc, fontsize=8, shadow=True)
    if grid:
        ax.grid()

    # show or save
    fig = ax.figure
    if show:
        plt.show()

    if save_path is not None:
        fig.savefig(save_path, dpi=dpi, bbox_inches="tight")
    else:
        return ax


def plot_misfit(
    misfit=None,
    misfit_data=None,
    misfit_model=None,
    xlim=[None, None],
    ylim=[None, None],
    show_misfit_model_iter0=True,
    markersize=2,
    log=True,
    grid=True,
    ax=None,
    figsize=(12, 6),
    show=True,
    save_path=None,
    dpi=100,
):
    ax = _get_ax(ax, figsize=figsize)

    if misfit_data is not None:
        if log:
            ax.semilogy(
                misfit_data,
                label="data",
                linestyle="--",
                marker="o",
                markersize=markersize + 2,
                color="blue",
                alpha=0.8,
            )
        else:
            ax.plot(
                misfit_data,
                label="data",
                linestyle="--",
                marker="o",
                markersize=markersize + 2,
                color="blue",
                alpha=0.8,
            )

    if misfit_model is not None:
        if not show_misfit_model_iter0:
            misfit_model = misfit_model[1:].copy()
            iters = np.arange(1, len(misfit_model) + 1)
        else:
            iters = np.arange(len(misfit_model))
        if log:
            ax.semilogy(
                iters,
                misfit_model,
                label="model",
                linestyle="--",
                marker="o",
                markersize=markersize + 2,
                color="green",
                alpha=0.8,
            )
        else:
            ax.plot(
                iters,
                misfit_model,
                label="model",
                linestyle="--",
                marker="o",
                markersize=markersize + 2,
                color="green",
                alpha=0.8,
            )

    if misfit is not None:
        if log:
            ax.semilogy(
                misfit,
                label="obj_value",
                linestyle="-",
                marker="o",
                markersize=markersize + 2,
                color="red",
                alpha=0.8,
            )
        else:
            ax.plot(
                misfit,
                label="obj_value",
                linestyle="-",
                marker="o",
                markersize=markersize + 2,
                color="red",
                alpha=0.8,
            )

    if not log:
        ax.ticklabel_format(style="sci", axis="y", scilimits=(-2, 2))
    ax.set_xlabel("Iterations")
    ax.set_ylabel("Misfit")
    ax.legend()
    if grid:
        ax.grid()

    if xlim[0] is not None and xlim[1] is not None:
        ax.set_xlim(xlim)

    ax.xaxis.set_major_locator(MaxNLocator(integer=True))

    if ylim[0] is not None and ylim[1] is not None:
        ax.set_ylim(ylim)

    # show or save
    fig = ax.figure
    if show:
        plt.show()

    if save_path is not None:
        fig.savefig(save_path, dpi=dpi, bbox_inches="tight")
    else:
        return ax


def plot_lcurve(
    misfit_data,
    misfit_model,
    smooth_factor,
    log=True,
    grid=True,
    ax=None,
    figsize=(12, 6),
    show=True,
    save_path=None,
    dpi=100,
):
    ax = _get_ax(ax, figsize=figsize)

    ax.plot(
        misfit_data,
        misfit_model,
        marker="o",
        linestyle="-",
        color="black",
        markersize=3,
    )

    for i in range(len(smooth_factor)):
        ax.text(
            misfit_data[i],
            misfit_model[i],
            f"{smooth_factor[i]:.1e}",
            fontsize=8,
            color="red",
        )

    ax.set_title("L-curve")
    ax.set_xlabel("Data misfit")
    ax.set_ylabel("Model misfit")

    if log:
        ax.set_xscale("log")
        ax.set_yscale("log")
    else:
        ax.ticklabel_format(style="sci", axis="both", scilimits=(-2, 2))

    if grid:
        ax.grid(True)

    if show:
        plt.show()

    fig = ax.figure
    if save_path is not None:
        fig.savefig(save_path, dpi=dpi, bbox_inches="tight")
    else:
        return ax
