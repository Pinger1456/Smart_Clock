"""Module for formatting the digital clock display."""


def format_display(sevseg_module):
    """
    Formats the seven-segment display output for the clock.

    :param hours: String representing the current hour.
    :param minutes: String representing the current minute.
    :param seconds: String representing the current second.
    :param sevseg_module: The module used to generate seven-segment strings.
    :return: A formatted string representing the digital clock display.
    """
    # Get digit strings from the sevseg module:
    h_top, h_middle, h_bottom = sevseg_module.get_sev_segstr().splitlines()
    m_top, m_middle, m_bottom = sevseg_module.get_sev_segstr().splitlines()
    s_top, s_middle, s_bottom = sevseg_module.get_sev_segstr().splitlines()

    # Build the formatted display string:
    display = (
        f"{h_top}     {m_top}     {s_top}\n"
        f"{h_middle}  *  {m_middle}  *  {s_middle}\n"
        f"{h_bottom}  *  {m_bottom}  *  {s_bottom}"
    )
    return display
