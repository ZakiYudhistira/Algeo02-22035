import { useState } from "react";
import { zodResolver } from "@hookform/resolvers/zod";
import { useForm } from "react-hook-form";
import * as z from "zod";
import axios, { AxiosError, AxiosResponse } from "axios";

import { Button } from "@/components/ui/button";
import {
  Form,
  FormControl,
  FormField,
  FormItem,
  FormMessage,
} from "@/components/ui/form";
import { Input } from "@/components/ui/input";

const formSchema = z.object({
  websiteUrl: z.string(),
});

const UrlForm = () => {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [success, setSuccess] = useState<string | null>(null);

  const form = useForm<z.infer<typeof formSchema>>({
    resolver: zodResolver(formSchema),
    defaultValues: {
      websiteUrl: "",
    },
  });

  async function onSubmit(values: z.infer<typeof formSchema>) {
    try {
      setLoading(true);
      setError(null);

      console.log("Encoded URL:", values.websiteUrl);
      const response = await axios.post<any, AxiosResponse<any>>(
        "http://127.0.0.1:5000/api/scrap",
        {
          url: values.websiteUrl,
        },
        {
          headers: {
            "Content-Type": "application/json",
          },
        }
      );

      console.log("Response:", response);

      if (response.status === 200) {
        const data = response.data;
        console.log(data.message);
        // Set success state
        setSuccess("Image scraping was successful!");
      } else {
        console.error("Image scraping failed");
        setError("Image scraping failed. Please try again.");
      }
    } catch (error) {
      console.error("An error occurred:", error);
      if (axios.isAxiosError(error)) {
        const axiosError = error as AxiosError;
        setError(`An error occurred: ${axiosError.message}`);
      } else {
        setError("An unexpected error occurred");
      }
    } finally {
      setLoading(false);
    }
  }

  return (
    <Form {...form}>
      <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-4">
        <h1 className="text-custom-green-dark font-montserrat text-[22px] font-extrabold">
          Image Scrapping
        </h1>
        <FormField
          control={form.control}
          name="websiteUrl"
          render={({ field }) => (
            <FormItem>
              <FormControl className="bg-gray-300">
                <Input placeholder="Website URL" {...field} />
              </FormControl>
              <FormMessage />
            </FormItem>
          )}
        />
        <Button
          type="submit"
          variant="outline"
          className="text-white bg-custom-black font-semibold rounded-xl px-5"
          disabled={loading}
        >
          {loading ? "Loading..." : "SUBMIT"}
        </Button>
        {error && (
          <p className="text-red-500 mt-2">
            <strong>Error:</strong> {error}
          </p>
        )}
        {success && (
          <p className="text-green-500 mt-2">
            <strong>Success:</strong> {success}
          </p>
        )}
      </form>
    </Form>
  );
};

export default UrlForm;
