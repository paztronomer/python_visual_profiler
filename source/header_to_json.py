"""
Script to dump into a JSON file the different extensions' headers of
FITS files. Useful to construct a template derived from a specific file.

"""
import argparse
import copy
import json
from astropy.io import fits

__author__ = "Francisco Paz-C"


def get_copy_header(filename):
    """
    Copy the different extension headers into a list of tuples
    being (extension_number, header_data)
    Parameters
    ----------
    filename : string
        Filename of FITS

    Returns
    -------
    hduall : list
        List of headers
    """
    hduall = []
    with fits.open(filename, "readonly") as hdulist:
        # In terms of complexity, remember enumerate() is an iterator,
        # so its complexity will be the number of elements it walks
        # through, and not necessarily the length of the list
        for idx, hdu in enumerate(hdulist):
            # Now, iterate over all the keywords in the header
            # and store:
            # - extension
            # - keyword
            # - value
            # - comment
            hdu_header = hdu.header

            for kw, val in hdu_header.items():
                # Get the comments
                try:
                    txt_comment = hdu_header.comments[kw]
                except:
                    txt_comment = ""

                # Fill a dictionary per keyword and append it to the
                # list to be serialised
                hduall.append(
                    {
                        "extension": idx + 1,
                        "keyword": kw,
                        "value": val,
                        "comment": txt_comment,
                    }
                )
    return hduall


def hdr_to_json(hlist,
                save2disk=True, outfnm="template.json"):
    """
    Writes JSON to disk and additionally returns a string with
    the converted dictionary

    Parameters
    ----------
    hlist : list
    save2disk : bool
    outfnm : str

    Returns
    -------
    outjson : str
        Parsed list of headers
    """

    if save2disk:
        try:
            with open(outfnm, "w+") as txt_json:
                # Write to disk
                json.dump(hlist, txt_json, indent=4)
            outjson = json.dumps(hlist)
        except:
            raise
    else:
        outjson = json.dumps(hlist)

    return outjson


def _get_args():
    """
    Simply get the args from function call

    Returns
    -------
    xarg : Namespace
    """
    txt_ini = "Use the input FITS file to construct a JSON containing"
    txt_ini += " the headers, to be used as template"
    arg = argparse.ArgumentParser(description=txt_ini,)
    #
    h1 = "FITS file from which headers will be extracted"
    arg.add_argument("fits", help=h1,)
    #
    h2 = "Filename for the output JSON (optional)"
    arg.add_argument("--outjson", help=h2)

    return arg.parse_args()


def _aux_main():
    """
    Helps declutter the main
    """
    arg = _get_args()

    # Copy headers
    hdu_list = get_copy_header(arg.fits)

    # Pass them to JSON encoder
    if arg.outjson is None:
        s_json = hdr_to_json(hdu_list, save2disk=True)
    else:
        s_json = hdr_to_json(hdu_list, save2disk=True,
                             outfnm=arg.outjson)


if __name__ == "__main__":

    _aux_main()